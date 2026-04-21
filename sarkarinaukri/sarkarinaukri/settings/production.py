from .base import *

import os
import dj_database_url

DEBUG = False

SECRET_KEY = os.environ.get('SECRET_KEY', 'your-secret-key-here')

ALLOWED_HOSTS = ['*']

DATABASES['default'] = dj_database_url.config(default='sqlite:///db.sqlite3')

MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# ManifestStaticFilesStorage is recommended in production, to prevent
# outdated JavaScript / CSS assets being served from cache
# (e.g. after a Wagtail upgrade).
# See https://docs.djangoproject.com/en/5.2/ref/contrib/staticfiles/#manifeststaticfilesstorage
STORAGES["staticfiles"]["BACKEND"] = "django.contrib.staticfiles.storage.ManifestStaticFilesStorage"

try:
    from .local import *
except ImportError:
    pass
