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
    'sarkarinaukriresult.online',
    'www.sarkarinaukriresult.online',
] + _extra_hosts

# WhiteNoise must come directly after SecurityMiddleware (index 1)
MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')

# CompressedStaticFilesStorage serves gzip-compressed files without a
# manifest. Safe with Wagtail (whose admin CSS has url() references that
# can confuse manifest post-processing). Cache-busting is handled via
# STATIC_VERSION query string in base.html instead.
STORAGES["staticfiles"]["BACKEND"] = "whitenoise.storage.CompressedStaticFilesStorage"

# Bump this string on every deploy to force browsers to re-fetch CSS/JS.
STATIC_VERSION = "4.1"

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
    'https://sarkarinaukriresult.online',
    'https://www.sarkarinaukriresult.online',
] + [
    f'https://{h}' for h in _extra_hosts if not h.startswith('http')
]

# Wagtail admin URL
WAGTAILADMIN_BASE_URL = "https://www.sarkarinaukriresult.online"

# Skip heavy sample data population during deployment
os.environ.setdefault('SKIP_SAMPLE_DATA', 'true')

# Logging: surface all errors to stderr so they appear in Railway's log stream.
# Without this, DEBUG=False silently swallows tracebacks and only returns 500.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '[{levelname}] {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'stderr': {
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
    },
    'root': {
        'handlers': ['stderr'],
        'level': 'WARNING',
    },
    'loggers': {
        'django': {
            'handlers': ['stderr'],
            'level': 'INFO',
            'propagate': False,
        },
        'django.request': {
            'handlers': ['stderr'],
            'level': 'ERROR',
            'propagate': False,
        },
        'django.security': {
            'handlers': ['stderr'],
            'level': 'ERROR',
            'propagate': False,
        },
    },
}

try:
    from .local import *
except ImportError:
    pass
