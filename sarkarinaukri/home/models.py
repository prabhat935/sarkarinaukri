from django.db import models
from wagtail.models import Page
from content.models import JobPosting, ExamResult, AdmitCard, Organization, ImportantNotification, AnswerKey


class HomePage(Page):
    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)

        # Latest jobs (2026 first, then 2025)
        context['latest_jobs'] = JobPosting.objects.select_related('organization').order_by('-year', '-application_end_date')[:12]

        # Recent results
        context['recent_results'] = ExamResult.objects.select_related('organization').order_by('-result_date')[:8]

        # Recent admit cards
        context['recent_admit_cards'] = AdmitCard.objects.select_related('organization').order_by('-admit_card_date')[:6]

        # Important notifications
        context['important_notifications'] = ImportantNotification.objects.order_by('-is_urgent', '-published_date')[:6]

        # Statistics
        context['latest_jobs_count'] = JobPosting.objects.filter(year=2026).count()
        context['recent_results_count'] = ExamResult.objects.filter(exam_year__gte=2024).count()
        context['admit_cards_count'] = AdmitCard.objects.count()
        context['notifications_count'] = ImportantNotification.objects.count()

        # Overall stats
        context['total_jobs'] = JobPosting.objects.count()
        context['total_results'] = ExamResult.objects.count()
        context['total_admit_cards'] = AdmitCard.objects.count()
        context['total_organizations'] = Organization.objects.count()

        # Featured organizations
        context['featured_organizations'] = Organization.objects.filter(is_featured=True)[:8]

        # Recent answer keys
        context['recent_answer_keys'] = AnswerKey.objects.select_related('organization').order_by('-exam_date')[:6]

        return context
