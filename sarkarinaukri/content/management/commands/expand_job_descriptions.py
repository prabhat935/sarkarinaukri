"""Expand thin job descriptions to improve AdSense content quality."""

from django.core.management.base import BaseCommand
from content.models import JobPosting


def generate_job_description(job):
    """Generate comprehensive job description based on available fields."""
    parts = []

    # Title and basic info
    parts.append(f"{job.title} recruitment notification has been released for the year {job.year}.")

    # Organization and category
    if job.organization:
        parts.append(f"The recruiting organization is {job.organization.name}.")
    if job.exam_category:
        parts.append(f"This recruitment falls under the {job.exam_category.name} category.")
    if job.state:
        parts.append(f"This job notification is for {job.state.name}.")

    # Vacancy and posting details
    if job.vacancies > 0:
        parts.append(f"A total of {job.vacancies} vacancies have been announced for this recruitment.")
    if job.job_level:
        parts.append(f"The post is classified as {job.get_job_level_display()}.")

    # Eligibility
    eligibility_parts = []
    if job.qualification_level:
        eligibility_parts.append(f"{job.qualification_level.get_level_display()} qualification is required")
    if job.min_age and job.max_age:
        eligibility_parts.append(f"age between {job.min_age} and {job.max_age} years")
    elif job.min_age:
        eligibility_parts.append(f"minimum age {job.min_age} years")
    elif job.max_age:
        eligibility_parts.append(f"maximum age {job.max_age} years")

    if eligibility_parts:
        parts.append(f"Candidates must have {', '.join(eligibility_parts)}.")

    if job.experience_required:
        parts.append(f"Experience requirement: {job.experience_required}")

    if job.gender_preference != 'Any':
        parts.append(f"Gender preference: {job.gender_preference} candidates.")

    # Salary information
    if job.salary_min and job.salary_max:
        parts.append(f"The salary range for this post is ₹{job.salary_min:,.0f} to ₹{job.salary_max:,.0f} per month, including all allowances.")
    elif job.salary_min:
        parts.append(f"The minimum salary for this post is ₹{job.salary_min:,.0f} per month.")

    # Application fee
    if job.application_fee:
        parts.append(f"Application fee: ₹{job.application_fee}. SC/ST and Female candidates may be eligible for fee exemption as per official guidelines.")

    # Important dates
    important_dates = []
    if job.application_start_date:
        important_dates.append(f"Application start date: {job.application_start_date.strftime('%d-%m-%Y')}")
    if job.application_end_date:
        important_dates.append(f"Application end date: {job.application_end_date.strftime('%d-%m-%Y')}")
    if job.exam_date:
        important_dates.append(f"Exam date: {job.exam_date.strftime('%d-%m-%Y')}")

    if important_dates:
        parts.append("Important dates: " + ", ".join(important_dates) + ".")

    # Selection process
    parts.append("The selection process typically includes written examination, document verification, and medical examination as applicable.")

    # Link to application
    if job.application_link:
        parts.append(f"Eligible candidates can apply online through the official website. The application must be completed before the deadline.")

    # Call to action
    parts.append(f"For complete details including full eligibility criteria, syllabus, exam pattern, and application procedure, refer to the official {job.organization.name} notification. Interested candidates should visit the official recruiting organization website for latest updates and to submit their applications.")

    return " ".join(parts)


def generate_meta_description(job):
    """Generate SEO-friendly meta description (max 160 chars)."""
    parts = []

    if job.title:
        parts.append(job.title[:50])
    if job.organization:
        parts.append(job.organization.name)
    if job.vacancies > 0:
        parts.append(f"{job.vacancies} vacancies")
    if job.exam_category:
        parts.append(job.exam_category.name)

    meta = " - ".join(parts)[:160]

    # Ensure it ends with period
    if not meta.endswith('.'):
        meta = meta[:157] + '.'

    return meta


class Command(BaseCommand):
    help = 'Expand thin job descriptions to improve AdSense content quality'

    def add_arguments(self, parser):
        parser.add_argument(
            '--all',
            action='store_true',
            help='Process all jobs, not just thin ones'
        )

    def handle(self, *args, **options):
        if options['all']:
            jobs_to_process = JobPosting.objects.all()
            self.stdout.write("Processing ALL jobs...")
        else:
            # Only process jobs with short descriptions
            jobs_to_process = JobPosting.objects.all()
            short_jobs = []
            for job in jobs_to_process:
                if len(job.description) < 200:
                    short_jobs.append(job)
            jobs_to_process = short_jobs
            self.stdout.write(f"Processing {len(short_jobs)} jobs with short descriptions...")

        updated = 0
        meta_added = 0

        for job in jobs_to_process:
            # Expand description if too short
            if len(job.description) < 200:
                new_desc = generate_job_description(job)
                job.description = new_desc
                updated += 1

            # Add meta description if missing
            if not job.meta_description or len(job.meta_description) < 10:
                job.meta_description = generate_meta_description(job)
                meta_added += 1

            job.save(update_fields=['description', 'meta_description'])

        self.stdout.write(self.style.SUCCESS(
            f'\nCompleted: {updated} descriptions expanded, {meta_added} meta descriptions added.'
        ))
