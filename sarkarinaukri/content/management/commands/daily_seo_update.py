"""
Management command: python manage.py daily_seo_update

Runs SEO maintenance tasks synchronously (no Celery required).
Called by start.sh on every deploy so fresh deployments are SEO-ready
immediately, and also scheduled as Celery beat tasks for ongoing updates.

Tasks:
  1. expire_old_jobs     — close jobs past their application deadline
  2. auto_fill_seo_meta  — fill blank meta_description on jobs & results
"""
from django.core.management.base import BaseCommand
from django.utils import timezone


class Command(BaseCommand):
    help = 'Run daily SEO update: expire jobs and fill meta descriptions'

    def handle(self, *args, **options):
        self.stdout.write('==> Daily SEO update started')

        # 1. Expire old jobs
        self.stdout.write('    [1/2] Expiring past-deadline jobs...')
        result = self._expire_old_jobs()
        self.stdout.write(self.style.SUCCESS(f'         {result}'))

        # 2. Auto-fill SEO meta
        self.stdout.write('    [2/2] Auto-filling SEO meta descriptions...')
        result = self._auto_fill_seo_meta()
        self.stdout.write(self.style.SUCCESS(f'         {result}'))

        self.stdout.write('==> Daily SEO update complete')

    # ------------------------------------------------------------------
    # Inline implementations (same logic as Celery tasks but synchronous)
    # ------------------------------------------------------------------

    def _expire_old_jobs(self):
        from content.models import JobPosting

        today = timezone.now().date()
        expired = JobPosting.objects.filter(
            status='Active',
            application_end_date__lt=today,
        )
        count = expired.update(status='Closed')
        return f'Expired {count} jobs'

    def _auto_fill_seo_meta(self):
        from content.models import JobPosting, ExamResult

        filled = 0

        jobs = JobPosting.objects.filter(meta_description='').select_related(
            'organization', 'state'
        )
        for job in jobs:
            parts = [f"Apply for {job.title}"]
            if job.organization:
                parts.append(f"at {job.organization}")
            if job.vacancies:
                parts.append(f"— {job.vacancies} vacancies")
            if job.application_end_date:
                parts.append(
                    f"Last date: {job.application_end_date.strftime('%d %b %Y')}"
                )
            if job.state:
                parts.append(f"| {job.state}")
            job.meta_description = '. '.join(parts)[:160]
            job.save(update_fields=['meta_description'])
            filled += 1

        results = ExamResult.objects.filter(meta_description='').select_related(
            'organization'
        )
        for result in results:
            desc = (
                f"Check {result.exam_name} {result.exam_year} result declared by "
                f"{result.organization}. Download result PDF and merit list."
            )[:160]
            result.meta_description = desc
            result.save(update_fields=['meta_description'])
            filled += 1

        return f'Filled SEO meta for {filled} items'

