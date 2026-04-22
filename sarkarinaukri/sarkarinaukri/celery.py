# sarkarinaukri/celery.py

import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sarkarinaukri.settings.production')

app = Celery('sarkarinaukri')

# Load configuration from Django settings, all keys in `CELERY_` namespace
app.config_from_object('django.conf:settings', namespace='CELERY')

# Auto-discover tasks from all registered Django app configs
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
