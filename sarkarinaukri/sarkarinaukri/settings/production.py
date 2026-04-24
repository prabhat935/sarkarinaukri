from .base import *
import os
import dj_database_url

DEBUG = False

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')  # set in Railway Variables

ALLOWED_HOSTS = ['sarkarinaukri-production.up.railway.app']

MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STORAGES["staticfiles"]["BACKEND"] = "django.contrib.staticfiles.storage.ManifestStaticFilesStorage"

# Database: use Railway's Postgres
DATABASES = {
    "default": dj_database_url.config(default=os.environ.get("DATABASE_URL"))
}

# Wagtail admin URL
WAGTAILADMIN_BASE_URL = "https://sarkarinaukri-production.up.railway.app"

# Skip heavy sample data population during deployment
os.environ.setdefault('SKIP_SAMPLE_DATA', 'true')

try:
    from .local import *
except ImportError:
    pass
