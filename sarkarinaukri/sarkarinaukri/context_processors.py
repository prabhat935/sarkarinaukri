"""
Context processors for passing global settings to templates
"""
from django.conf import settings


def content_section_flags():
    """
    Which optional sections have something to show. Empty sections are hidden
    from navigation and the sitemap so visitors never land on a blank page.
    """
    from content.models import (
        FAQ, AdmitCard, AnswerKey, ExamResult, ImportantNotification, OnlineForm,
        Scholarship, Syllabus,
    )

    return {
        'has_scholarships': Scholarship.objects.filter(status='Open').exists(),
        'has_notifications': ImportantNotification.objects.exists(),
        'has_online_forms': OnlineForm.objects.filter(status='Active').exists(),
        'has_faqs': FAQ.objects.exists(),
        # Results, admit cards, answer keys and syllabus count only when an
        # entry has a real write-up, not just a title and a link
        'has_results': bool(ExamResult.listed()),
        'has_admit_cards': bool(AdmitCard.listed()),
        'has_answer_keys': bool(AnswerKey.listed()),
        'has_syllabus': bool(Syllabus.listed()),
        # Board results are bare links to board websites with no write-up
        'has_board_results': False,
    }


def monetization_context(request):
    """
    Add monetization settings (Google AdSense, Analytics) to template context
    """
    return {
        'google_adsense_client_id': settings.GOOGLE_ADSENSE_CLIENT_ID,
        'google_adsense_enabled': settings.GOOGLE_ADSENSE_ENABLED,
        'google_analytics_id': settings.GOOGLE_ANALYTICS_ID,
        'site_name': settings.SITE_NAME,
        'site_description': settings.SITE_DESCRIPTION,
        'site_keywords': settings.SITE_KEYWORDS,
        'static_version': getattr(settings, 'STATIC_VERSION', '1'),
        **content_section_flags(),
    }
