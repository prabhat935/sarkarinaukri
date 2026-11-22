"""
Manually tell Google (Indexing API) and Bing (IndexNow) about job pages.

  python manage.py ping_search_engines --active   # every open job
  python manage.py ping_search_engines --job 380 --job 379
  python manage.py ping_search_engines --url https://www.sarkarinaukriresult.online/content/faq/

--url pages go to IndexNow only: Google's Indexing API is for job pages.
Google allows about 200 notifications a day, so avoid repeating --active.
"""
from django.core.management.base import BaseCommand

from content.models import JobPosting
from content.search_ping import notify, notify_jobs


class Command(BaseCommand):
    help = 'Ping Google Indexing API and IndexNow for job pages'

    def add_arguments(self, parser):
        parser.add_argument('--active', action='store_true', help='all open, indexable jobs')
        parser.add_argument('--job', type=int, action='append', default=[], help='job id (repeatable)')
        parser.add_argument('--url', action='append', default=[], help='non-job URL, IndexNow only')

    def handle(self, *args, **opts):
        jobs = list(JobPosting.objects.filter(pk__in=opts['job']))
        if opts['active']:
            # Only pages Google may index: open jobs with a real write-up
            jobs += [j for j in JobPosting.indexable() if j.pk not in opts['job']]
        if jobs:
            self.stdout.write(f'Jobs: {[j.pk for j in jobs]}')
            self.stdout.write(str(notify_jobs(jobs, force=True, background=False)))
        if opts['url']:
            self.stdout.write(str(notify(opts['url'], google=False, force=True, background=False)))
        if not jobs and not opts['url']:
            self.stdout.write('Nothing to send. Use --active, --job or --url.')
