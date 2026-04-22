# notifications/views.py

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from .models import UserPreference


@login_required
def preferences(request):
    """User notification preferences page"""
    
    pref, created = UserPreference.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        # Update preferences
        pref.email_alerts = request.POST.get('email_alerts') == 'on'
        pref.sms_alerts = request.POST.get('sms_alerts') == 'on'
        pref.push_notifications = request.POST.get('push_notifications') == 'on'
        pref.whatsapp_alerts = request.POST.get('whatsapp_alerts') == 'on'
        pref.alert_frequency = request.POST.get('alert_frequency', 'daily')
        pref.phone_number = request.POST.get('phone_number', '')
        
        # Update interests
        states = request.POST.getlist('states')
        categories = request.POST.getlist('categories')
        organizations = request.POST.getlist('organizations')
        
        pref.selected_states.set(states)
        pref.selected_categories.set(categories)
        pref.selected_organizations.set(organizations)
        
        pref.save()
        
        return render(request, 'notifications/preferences.html', {
            'pref': pref,
            'message': 'Preferences updated successfully!'
        })
    
    from content.models import State, ExamCategory, Organization
    
    context = {
        'pref': pref,
        'states': State.objects.all(),
        'categories': ExamCategory.objects.all(),
        'organizations': Organization.objects.all(),
        'frequencies': UserPreference.FREQUENCY_CHOICES,
    }
    
    return render(request, 'notifications/preferences.html', context)


@login_required
@require_POST
def save_job(request, job_id):
    """Save/unsave a job (AJAX)"""
    from content.models import JobPosting, SavedJob
    
    try:
        job = JobPosting.objects.get(id=job_id)
        saved_job, created = SavedJob.objects.get_or_create(
            user=request.user,
            job=job
        )
        
        if not created:
            saved_job.delete()
            return JsonResponse({'status': 'unsaved'})
        
        return JsonResponse({'status': 'saved'})
    
    except JobPosting.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Job not found'}, status=404)
