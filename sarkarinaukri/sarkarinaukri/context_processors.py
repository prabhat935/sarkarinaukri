"""
Context processors for passing global settings to templates
"""
from django.conf import settings


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
    }
