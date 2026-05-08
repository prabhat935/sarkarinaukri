# notifications/tasks.py

from celery import shared_task
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from .models import UserPreference, NotificationLog, NotificationTemplate, AlertRule
from content.models import JobPosting, ExamResult, AdmitCard, AnswerKey


@shared_task
def send_job_alert_email(user_id, job_ids):
    """Send email with job alerts to a user"""
    try:
        user = User.objects.get(id=user_id)
        pref = user.notification_preference
        
        if not pref.email_alerts:
            return False
        
        jobs = JobPosting.objects.filter(id__in=job_ids)
        
        # Render email template
        context = {
            'user': user,
            'jobs': jobs,
            'job_count': len(jobs)
        }
        
        subject = f"New Job Alerts - {len(jobs)} matching jobs"
        html_message = render_to_string('notifications/email/job_alert.html', context)
        message = strip_tags(html_message)
        
        # Send email
        send_mail(
            subject,
            message,
            'noreply@sarkarinaukri.com',
            [user.email],
            html_message=html_message,
            fail_silently=False,
        )
        
        # Log notification
        NotificationLog.objects.create(
            user=user,
            channel='email',
            subject=subject,
            message=f"Sent {len(jobs)} job alerts",
            status='sent',
            sent_at=datetime.now()
        )
        
        return True
        
    except Exception as e:
        NotificationLog.objects.create(
            user_id=user_id,
            channel='email',
            subject='Job Alert',
            message='Failed to send job alert',
            status='failed',
            error_message=str(e)
        )
        return False


@shared_task
def send_daily_job_digest():
    """Send daily digest of new jobs to all subscribed users"""
    
    # Get all users who want daily emails
    users = User.objects.filter(
        notification_preference__email_alerts=True,
        notification_preference__alert_frequency='daily'
    )
    
    for user in users:
        pref = user.notification_preference
        
        # Get jobs from last 24 hours matching user preferences
        jobs = JobPosting.objects.filter(
            created_at__gte=datetime.now() - timedelta(days=1),
            status='Active'
        )
        
        if pref.selected_states.exists():
            jobs = jobs.filter(state__in=pref.selected_states.all())
        
        if pref.selected_categories.exists():
            jobs = jobs.filter(exam_category__in=pref.selected_categories.all())
        
        if pref.selected_organizations.exists():
            jobs = jobs.filter(organization__in=pref.selected_organizations.all())
        
        if jobs.exists():
            job_ids = list(jobs.values_list('id', flat=True))
            send_job_alert_email.delay(user.id, job_ids)


@shared_task
def send_sms_alert(phone_number, message):
    """Send SMS alert via Twilio"""
    try:
        from twilio.rest import Client
        import os
        
        account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
        auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
        twilio_phone = os.environ.get('TWILIO_PHONE_NUMBER')
        
        if not all([account_sid, auth_token, twilio_phone]):
            return False
        
        client = Client(account_sid, auth_token)
        message_obj = client.messages.create(
            body=message,
            from_=twilio_phone,
            to=phone_number
        )
        
        return True
        
    except Exception as e:
        print(f"SMS sending failed: {str(e)}")
        return False


@shared_task
def process_alert_rules():
    """Process alert rules and send notifications"""
    
    rules = AlertRule.objects.filter(is_active=True)
    
    for rule in rules:
        if rule.alert_type == 'new_job':
            # Check for new jobs matching the rule
            jobs = JobPosting.objects.filter(
                created_at__gte=datetime.now() - timedelta(hours=1),
                status='Active'
            )
            
            if rule.state:
                jobs = jobs.filter(state=rule.state)
            if rule.exam_category:
                jobs = jobs.filter(exam_category=rule.exam_category)
            if rule.organization:
                jobs = jobs.filter(organization=rule.organization)
            
            # Send to subscribed users
            for user in rule.notify_users.all():
                job_ids = list(jobs.values_list('id', flat=True))
                if job_ids:
                    send_job_alert_email.delay(user.id, job_ids)


@shared_task
def cleanup_old_notifications():
    """Delete notifications older than 90 days"""
    from datetime import timedelta
    from django.utils import timezone

    cutoff_date = timezone.now() - timedelta(days=90)
    NotificationLog.objects.filter(created_at__lt=cutoff_date).delete()


# ============= DAILY SEO TASKS =============

@shared_task
def expire_old_jobs():
    """
    Mark Active jobs as Closed when their application_end_date has passed.
    Runs daily so search engines immediately see accurate status and
    we stop serving stale 'Active' listings.
    """
    from django.utils import timezone

    today = timezone.now().date()
    expired = JobPosting.objects.filter(
        status='Active',
        application_end_date__lt=today,
    )
    count = expired.update(status='Closed')
    return f"Expired {count} jobs"


@shared_task
def auto_fill_seo_meta():
    """
    Auto-generate meta_description for jobs/results that have it empty.
    Fills only blank fields so manually edited descriptions are preserved.
    Runs daily so every new item gets SEO meta within 24 hours.
    """
    from django.utils import timezone

    year = timezone.now().year
    filled = 0

    # --- Job postings ---
    jobs = JobPosting.objects.filter(meta_description='').select_related(
        'organization', 'state', 'exam_category'
    )
    for job in jobs:
        parts = [f"Apply for {job.title}"]
        if job.organization:
            parts.append(f"at {job.organization}")
        if job.vacancies:
            parts.append(f"— {job.vacancies} vacancies")
        if job.application_end_date:
            parts.append(f"Last date: {job.application_end_date.strftime('%d %b %Y')}")
        if job.state:
            parts.append(f"| {job.state}")
        desc = '. '.join(parts)[:160]
        job.meta_description = desc
        job.save(update_fields=['meta_description'])
        filled += 1

    # --- Exam results ---
    results = ExamResult.objects.filter(meta_description='').select_related('organization')
    for result in results:
        desc = (
            f"Check {result.exam_name} {result.exam_year} result declared by "
            f"{result.organization}. Download result PDF and merit list."
        )[:160]
        result.meta_description = desc
        result.save(update_fields=['meta_description'])
        filled += 1

    # --- Admit cards ---
    from content.models import AdmitCard
    for card in AdmitCard.objects.select_related('organization'):
        # AdmitCard has no meta_description field — skip silently
        pass

    return f"Filled SEO meta for {filled} items"


