"""
Context processors for passing global settings to templates
"""
from django.conf import settings


def content_section_flags():
    """
    Which optional sections have something to show. Empty sections are hidden
    from navigation and the sitemap so visitors never land on a blank page.
    """
    from content.models import FAQ, ImportantNotification, OnlineForm, Scholarship

    return {
        'has_scholarships': Scholarship.objects.filter(status='Open').exists(),
        'has_notifications': ImportantNotification.objects.exists(),
        'has_online_forms': OnlineForm.objects.filter(status='Active').exists(),
        'has_faqs': FAQ.objects.exists(),
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
