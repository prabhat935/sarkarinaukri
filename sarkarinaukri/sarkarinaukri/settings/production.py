from .base import *
import os
import dj_database_url

DEBUG = False

# SECRET_KEY must be set via the DJANGO_SECRET_KEY environment variable in Railway.
# Django will refuse to start if this is empty or None.
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')
if not SECRET_KEY:
    raise ValueError(
        "The DJANGO_SECRET_KEY environment variable is not set. "
        "Add it to your Railway service variables."
    )

# Accept the hardcoded Railway domain plus any host supplied via ALLOWED_HOSTS env var
# (comma-separated). Also accept Railway's internal *.railway.app wildcard.
_extra_hosts = [
    h.strip()
    for h in os.environ.get('ALLOWED_HOSTS', '').split(',')
    if h.strip()
]
ALLOWED_HOSTS = [
    'gleaming-generosity-production-22ba.up.railway.app',
    '.railway.app',
] + _extra_hosts

# WhiteNoise must come directly after SecurityMiddleware (index 1)
MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')

# Use WhiteNoise's compressed+hashed storage for static files.
# Do NOT also set the legacy STATICFILES_STORAGE — it conflicts with STORAGES.
STORAGES["staticfiles"]["BACKEND"] = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Database: use Railway's Postgres via DATABASE_URL
_database_url = os.environ.get("DATABASE_URL")
if not _database_url:
    raise ValueError(
        "The DATABASE_URL environment variable is not set. "
        "Add a Postgres database to your Railway project and link it to this service."
    )
DATABASES = {
    "default": dj_database_url.config(default=_database_url, conn_max_age=600)
}

# Trust Railway's HTTPS origins for CSRF
CSRF_TRUSTED_ORIGINS = [
    'https://gleaming-generosity-production-22ba.up.railway.app',
    'https://*.railway.app',
] + [
    f'https://{h}' for h in _extra_hosts if not h.startswith('http')
]

# Wagtail admin URL
WAGTAILADMIN_BASE_URL = "https://gleaming-generosity-production-22ba.up.railway.app"

# Skip heavy sample data population during deployment
os.environ.setdefault('SKIP_SAMPLE_DATA', 'true')

try:
    from .local import *
except ImportError:
    pass
