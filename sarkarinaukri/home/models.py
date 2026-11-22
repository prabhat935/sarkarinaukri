from datetime import date, timedelta

from django.db import models
from django.db.models import Q
from wagtail.models import Page
from content.models import (
    JobPosting, ExamResult, AdmitCard, Organization, ImportantNotification, AnswerKey, Article,
    MIN_INDEXABLE_WORDS, word_count,
)


class HomePage(Page):
    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)

        # Latest open jobs, soonest-closing last date first
        context['latest_jobs'] = JobPosting.objects.select_related('organization').filter(
            status='Active'
        ).order_by('application_end_date')[:12]
        context['active_jobs_count'] = JobPosting.objects.filter(status='Active').count()

        # Latest exam guides
        context['latest_articles'] = Article.published()[:6]
        context['total_articles'] = Article.published().count()

        # Recent results
        # Only entries with a real write-up; title-and-link placeholders stay hidden
        listed_results = ExamResult.listed(ExamResult.objects.select_related('organization').order_by('-result_date'))
        listed_admit_cards = AdmitCard.listed(AdmitCard.objects.select_related('organization').order_by('-admit_card_date'))
        context['recent_results'] = listed_results[:8]

        # Recent admit cards
        context['recent_admit_cards'] = listed_admit_cards[:6]

        # Important notifications
        context['important_notifications'] = ImportantNotification.objects.order_by('-is_urgent', '-published_date')[:6]

        # Statistics
        context['latest_jobs_count'] = JobPosting.objects.filter(year=2026).count()
        context['recent_results_count'] = len(listed_results)
        context['admit_cards_count'] = len(listed_admit_cards)
        context['notifications_count'] = ImportantNotification.objects.count()

        # Overall stats
        context['total_jobs'] = JobPosting.objects.count()
        context['total_results'] = len(listed_results)
        context['total_admit_cards'] = len(listed_admit_cards)
        context['total_organizations'] = Organization.objects.count()

        # Featured organizations
        context['featured_organizations'] = Organization.objects.filter(is_featured=True)[:8]

        # Recent answer keys
        context['recent_answer_keys'] = AnswerKey.listed(AnswerKey.objects.select_related('organization').order_by('-exam_date'))[:6]

        # Top-of-page scrolling lines: open jobs, three per line
        top = list(context['latest_jobs'][:9])
        context['highlight_lines'] = [top[i:i + 3] for i in range(0, len(top), 3)]

        context.update(job_highlights())
        context['guides_by_topic'] = guides_by_topic()

        return context


# Homepage qualification buttons: (key, label, icon). "engineering" is matched
# on the job category; the rest on the job's qualification level.
QUALIFICATION_BUCKETS = [
    ('10th', '10th / ITI', 'fa-tools'),
    ('12th', '12th Pass', 'fa-school'),
    ('graduate', 'Graduate', 'fa-user-graduate'),
    ('engineering', 'Engineering', 'fa-cogs'),
    ('pg', 'PG / CA / MBA', 'fa-briefcase'),
]


def _written_up(job):
    """A post with a real write-up, not an old one-line placeholder."""
    return word_count(job.description) >= MIN_INDEXABLE_WORDS


def job_highlights(today=None):
    """Closing soon, newly added, qualification counts, upcoming exams and
    recently closed jobs, all built from job posts that have a real write-up."""
    today = today or date.today()
    open_jobs = list(JobPosting.indexable().select_related('organization', 'exam_category', 'qualification_level'))
    open_jobs = [j for j in open_jobs if _written_up(j)]

    closing_soon = sorted(
        [j for j in open_jobs if j.application_end_date and 0 <= (j.application_end_date - today).days <= 10],
        key=lambda j: j.application_end_date,
    )

    newly_added = sorted(open_jobs, key=lambda j: j.created_at, reverse=True)[:6]
    for j in newly_added:
        j.is_new = (today - j.created_at.date()).days <= 7

    qualification_counts = []
    for key, label, icon in QUALIFICATION_BUCKETS:
        if key == 'engineering':
            n = sum(1 for j in open_jobs if j.exam_category and j.exam_category.slug == 'engineering')
        else:
            n = sum(1 for j in open_jobs if j.qualification_level and j.qualification_level.level == key)
        qualification_counts.append({'key': key, 'label': label, 'icon': icon, 'count': n})

    recent_window = today - timedelta(days=45)
    written = [
        j for j in JobPosting.objects.select_related('organization').filter(
            Q(exam_date__gte=today) | Q(status='Closed', application_end_date__gte=recent_window)
        )
        if _written_up(j)
    ]
    upcoming_exams = sorted([j for j in written if j.exam_date and j.exam_date >= today], key=lambda j: j.exam_date)[:8]
    for j in upcoming_exams:
        j.days_to_exam = (j.exam_date - today).days

    recently_closed = sorted(
        [j for j in written if j.status == 'Closed' and j.application_end_date and j.application_end_date >= recent_window],
        key=lambda j: j.application_end_date, reverse=True,
    )[:6]
    for j in recently_closed:
        if j.exam_date and j.exam_date >= today:
            j.next_step = f"Exam on {j.exam_date.strftime('%d %b %Y')}"
        else:
            j.next_step = 'Admit card and exam date awaited'

    return {
        'closing_soon': closing_soon[:8],
        'newly_added': newly_added,
        'qualification_counts': qualification_counts,
        'upcoming_exams': upcoming_exams,
        'recently_closed': recently_closed,
    }


GUIDE_TOPICS = [
    ('exam-guide', 'Exam Guides', 'fa-book'),
    ('preparation', 'Preparation Tips', 'fa-pencil-alt'),
    ('career', 'Career and Salary', 'fa-briefcase'),
    ('news', 'News and Updates', 'fa-newspaper'),
]


def guides_by_topic():
    """Every published guide, grouped by topic, newest first."""
    articles = list(Article.published())
    groups = []
    for key, label, icon in GUIDE_TOPICS:
        items = [a for a in articles if a.category == key]
        if items:
            groups.append({'key': key, 'label': label, 'icon': icon, 'articles': items})
    return groups
