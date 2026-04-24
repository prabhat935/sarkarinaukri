from .base import *

import os

DEBUG = False

SECRET_KEY = os.environ.get('SECRET_KEY', 'your-secret-key-here')

ALLOWED_HOSTS = ['*']

MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# ManifestStaticFilesStorage is recommended in production, to prevent
# outdated JavaScript / CSS assets being served from cache
# (e.g. after a Wagtail upgrade).
# See https://docs.djangoproject.com/en/5.2/ref/contrib/staticfiles/#manifeststaticfilesstorage
STORAGES["staticfiles"]["BACKEND"] = "django.contrib.staticfiles.storage.ManifestStaticFilesStorage"

# Skip heavy sample data population during deployment to avoid timeouts
os.environ.setdefault('SKIP_SAMPLE_DATA', 'true')

try:
    from .local import *
except ImportError:
    pass
