# content/models.py

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# ============= REFERENCE MODELS =============

class Organization(models.Model):
    """Government organizations conducting exams"""
    name = models.CharField(max_length=100, unique=True, db_index=True)  # SSC, UPSC, BPSC, etc.
    slug = models.SlugField(unique=True, db_index=True)
    description = models.TextField(blank=True)
    website = models.URLField(blank=True)
    logo = models.ImageField(upload_to='org_logos/', blank=True, null=True)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-is_featured', 'name']
        verbose_name_plural = "Organizations"

    def __str__(self):
        return self.name


class ExamCategory(models.Model):
    """Exam categories: Bank, Police, Teaching, etc."""
    name = models.CharField(max_length=100, unique=True, db_index=True)
    slug = models.SlugField(unique=True, db_index=True)
    description = models.TextField(blank=True)
    icon = models.CharField(max_length=50, blank=True)  # FontAwesome icon class
    is_featured = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Exam Categories"
        ordering = ['-is_featured', 'name']

    def __str__(self):
        return self.name


class State(models.Model):
    """Indian states"""
    name = models.CharField(max_length=50, unique=True, db_index=True)  # Uttar Pradesh, Bihar
    code = models.CharField(max_length=2, unique=True)  # UP, BH
    is_featured = models.BooleanField(default=False)

    class Meta:
        ordering = ['-is_featured', 'name']

    def __str__(self):
        return self.name


class QualificationLevel(models.Model):
    """Education levels"""
    LEVELS = [
        ('10th', '10th Pass'),
        ('12th', '12th Pass'),
        ('graduate', 'Graduate'),
        ('pg', 'Post Graduate'),
        ('phd', 'Ph.D'),
    ]
    level = models.CharField(max_length=20, unique=True, choices=LEVELS)

    class Meta:
        verbose_name_plural = "Qualification Levels"

    def __str__(self):
        return self.get_level_display()


# ============= MAIN CONTENT MODELS =============

class JobPosting(models.Model):
    """Government job notifications"""
    
    # Basic Info
    title = models.CharField(max_length=200, db_index=True)
    description = models.TextField()
    slug = models.SlugField(unique=True, db_index=True)
    
    # Organization & Category
    organization = models.ForeignKey(Organization, on_delete=models.PROTECT)
    exam_category = models.ForeignKey(ExamCategory, on_delete=models.SET_NULL, null=True, blank=True)
    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True, blank=True)
    
    # Job Details
    vacancies = models.PositiveIntegerField(default=0)
    job_level = models.CharField(
        max_length=20,
        choices=[('A', 'Group A'), ('B', 'Group B'), ('C', 'Group C'), ('D', 'Group D')],
        blank=True,
        db_index=True
    )
    qualification_level = models.ForeignKey(QualificationLevel, on_delete=models.SET_NULL, null=True, blank=True)
    min_age = models.PositiveIntegerField(null=True, blank=True)
    max_age = models.PositiveIntegerField(null=True, blank=True)
    salary_min = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    salary_max = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    
    # Eligibility
    eligibility = models.TextField(blank=True)
    experience_required = models.CharField(max_length=100, blank=True)
    gender_preference = models.CharField(
        max_length=20,
        choices=[('Any', 'Any'), ('Male', 'Male Only'), ('Female', 'Female Only')],
        default='Any'
    )
    
    # Important Dates
    application_start_date = models.DateField(null=True, blank=True, db_index=True)
    application_end_date = models.DateField(null=True, blank=True, db_index=True)
    exam_date = models.DateField(null=True, blank=True)
    interview_date = models.DateField(null=True, blank=True)
    result_date = models.DateField(null=True, blank=True)
    
    # Application Info
    application_link = models.URLField(blank=True)
    application_fee = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    
    # Status & Timestamps
    status = models.CharField(
        max_length=20,
        choices=[
            ('Active', 'Active'),
            ('Closed', 'Closed'),
            ('Postponed', 'Postponed'),
            ('Cancelled', 'Cancelled'),
        ],
        default='Active',
        db_index=True
    )
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # SEO
    meta_description = models.CharField(max_length=160, blank=True, help_text="Google meta description")
    meta_keywords = models.CharField(max_length=160, blank=True)

    class Meta:
        ordering = ['-application_end_date', '-created_at']
        indexes = [
            models.Index(fields=['state', '-created_at']),
            models.Index(fields=['organization', '-created_at']),
            models.Index(fields=['exam_category', '-created_at']),
        ]

    def __str__(self):
        return self.title

    @property
    def days_remaining(self):
        from datetime import date
        if self.application_end_date:
            return (self.application_end_date - date.today()).days
        return None


class ExamResult(models.Model):
    """Published exam results"""
    
    exam_name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(unique=True, db_index=True)
    description = models.TextField(blank=True)
    
    organization = models.ForeignKey(Organization, on_delete=models.PROTECT)
    exam_category = models.ForeignKey(ExamCategory, on_delete=models.SET_NULL, null=True, blank=True)
    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True, blank=True)
    
    exam_year = models.IntegerField(db_index=True)
    result_date = models.DateField(null=True, blank=True, db_index=True)
    
    # Result files
    result_pdf_link = models.URLField(blank=True, help_text="Direct link to result PDF")
    merit_list_link = models.URLField(blank=True)
    cutoff_marks_link = models.URLField(blank=True)
    
    # Additional info
    total_posts = models.PositiveIntegerField(null=True, blank=True)
    selected_candidates = models.PositiveIntegerField(null=True, blank=True)
    
    # Status
    is_official = models.BooleanField(default=False)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    meta_description = models.CharField(max_length=160, blank=True)

    class Meta:
        ordering = ['-exam_year', '-result_date']
        unique_together = ['exam_name', 'exam_year']

    def __str__(self):
        return f"{self.exam_name} {self.exam_year}"


class AdmitCard(models.Model):
    """Admit card information and downloads"""
    
    exam_name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(unique=True, db_index=True)
    description = models.TextField(blank=True)
    
    organization = models.ForeignKey(Organization, on_delete=models.PROTECT)
    exam_category = models.ForeignKey(ExamCategory, on_delete=models.SET_NULL, null=True, blank=True)
    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True, blank=True)
    
    exam_date = models.DateField(db_index=True)
    admit_card_date = models.DateField()
    download_link = models.URLField()
    exam_time = models.TimeField(null=True, blank=True)
    exam_duration = models.CharField(max_length=20, blank=True, help_text="e.g., 2 hours")
    
    # Important instructions
    instructions = models.TextField(blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-admit_card_date']

    def __str__(self):
        return f"{self.exam_name} - Admit Card"


class AnswerKey(models.Model):
    """Exam answer keys"""
    
    exam_name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(db_index=True)
    description = models.TextField(blank=True)
    
    organization = models.ForeignKey(Organization, on_delete=models.PROTECT)
    exam_category = models.ForeignKey(ExamCategory, on_delete=models.SET_NULL, null=True, blank=True)
    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True, blank=True)
    
    exam_year = models.IntegerField(db_index=True)
    exam_date = models.DateField()
    publication_date = models.DateField(auto_now_add=True)
    
    # Answer key details
    shift_number = models.PositiveIntegerField(default=1, help_text="For multiple shifts")
    question_paper_link = models.URLField(blank=True)
    answer_key_link = models.URLField()
    solution_pdf_link = models.URLField(blank=True)
    
    # Status
    is_official = models.BooleanField(default=False)
    is_provisional = models.BooleanField(default=False)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-exam_date']
        unique_together = ['exam_name', 'exam_year', 'shift_number']

    def __str__(self):
        return f"{self.exam_name} - Answer Key"


class Syllabus(models.Model):
    """Exam syllabus and study material"""
    
    exam_name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(unique=True, db_index=True)
    
    organization = models.ForeignKey(Organization, on_delete=models.PROTECT)
    exam_category = models.ForeignKey(ExamCategory, on_delete=models.SET_NULL, null=True, blank=True)
    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True, blank=True)
    
    # Syllabus details
    exam_year = models.IntegerField()
    subjects = models.TextField(help_text="Comma-separated list of subjects")
    detailed_syllabus_link = models.URLField(blank=True)
    
    # Study material
    important_topics = models.TextField(blank=True)
    previous_papers_link = models.URLField(blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-exam_year']
        verbose_name_plural = "Syllabi"

    def __str__(self):
        return f"{self.exam_name} - Syllabus"


class AdmissionForm(models.Model):
    """College/University admission forms"""
    
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(unique=True, db_index=True)
    
    institution_name = models.CharField(max_length=200)
    exam_category = models.ForeignKey(ExamCategory, on_delete=models.SET_NULL, null=True, blank=True)
    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True, blank=True)
    
    # Important dates
    form_start_date = models.DateField()
    form_end_date = models.DateField()
    merit_list_date = models.DateField(null=True, blank=True)
    counselling_date = models.DateField(null=True, blank=True)
    
    # Form details
    form_link = models.URLField()
    application_fee = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    eligibility = models.TextField(blank=True)
    
    # Status
    status = models.CharField(
        max_length=20,
        choices=[
            ('Open', 'Open'),
            ('Closed', 'Closed'),
            ('Postponed', 'Postponed'),
        ],
        default='Open'
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-form_start_date']

    def __str__(self):
        return self.name


class CertificateVerification(models.Model):
    """Certificate verification links"""
    
    exam_name = models.CharField(max_length=200, unique=True, db_index=True)
    slug = models.SlugField(unique=True, db_index=True)
    
    organization = models.ForeignKey(Organization, on_delete=models.PROTECT)
    exam_category = models.ForeignKey(ExamCategory, on_delete=models.SET_NULL, null=True, blank=True)
    
    verification_link = models.URLField()
    year = models.IntegerField(null=True, blank=True)
    
    instructions = models.TextField(blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.exam_name} - Certificate Verification"


class BoardExamResult(models.Model):
    """School board exam results (10th, 12th, etc.)"""
    
    BOARD_CHOICES = [
        ('CBSE', 'Central Board of Secondary Education'),
        ('ICSE', 'Indian Certificate of Secondary Education'),
        ('UP Board', 'Uttar Pradesh Board'),
        ('Bihar Board', 'Bihar School Examination Board'),
        ('MP Board', 'Madhya Pradesh Board'),
        ('Rajasthan Board', 'Rajasthan Board of Secondary Education'),
        ('Haryana Board', 'Haryana Board of School Education'),
        ('Punjab Board', 'Punjab School Education Board'),
        ('Gujarat Board', 'Gujarat Secondary and Higher Secondary Education Board'),
        ('Maharashtra Board', 'Maharashtra State Board of Secondary and Higher Secondary Education'),
    ]
    
    board = models.CharField(max_length=20, choices=BOARD_CHOICES)
    exam_type = models.CharField(max_length=10, choices=[('10th', 'Class 10th'), ('12th', 'Class 12th')])
    year = models.IntegerField()
    
    result_link = models.URLField(help_text="Direct link to board result website")
    digilocker_link = models.URLField(blank=True, help_text="DigiLocker verification link")
    
    result_date = models.DateField()
    is_declared = models.BooleanField(default=False)
    
    total_students = models.PositiveIntegerField(null=True, blank=True)
    pass_percentage = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-result_date']
        unique_together = ['board', 'exam_type', 'year']

    def __str__(self):
        return f"{self.board} {self.exam_type} Result {self.year}"


class Scholarship(models.Model):
    """Government scholarships"""
    
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(unique=True, db_index=True)
    
    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True, blank=True)
    category = models.CharField(
        max_length=20,
        choices=[
            ('SC/ST', 'SC/ST Scholarship'),
            ('OBC', 'OBC Scholarship'),
            ('Minority', 'Minority Scholarship'),
            ('Merit', 'Merit Scholarship'),
            ('General', 'General Scholarship'),
        ]
    )
    
    application_start_date = models.DateField()
    application_end_date = models.DateField()
    application_link = models.URLField()
    
    eligibility = models.TextField()
    benefits = models.TextField()
    documents_required = models.TextField(blank=True)
    
    status = models.CharField(
        max_length=20,
        choices=[
            ('Open', 'Open'),
            ('Closed', 'Closed'),
            ('Coming Soon', 'Coming Soon'),
        ],
        default='Open'
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-application_end_date']

    def __str__(self):
        return self.name


class ImportantNotification(models.Model):
    """Important government notifications and updates"""
    
    title = models.CharField(max_length=300, db_index=True)
    slug = models.SlugField(unique=True, db_index=True)
    
    category = models.CharField(
        max_length=50,
        choices=[
            ('Government', 'Government Notification'),
            ('Exam', 'Exam Notification'),
            ('Admission', 'Admission Notification'),
            ('Recruitment', 'Recruitment Notification'),
            ('Policy', 'Policy Update'),
            ('Other', 'Other'),
        ]
    )
    
    description = models.TextField()
    notification_link = models.URLField(blank=True)
    pdf_link = models.URLField(blank=True)
    
    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True, blank=True)
    organization = models.ForeignKey(Organization, on_delete=models.SET_NULL, null=True, blank=True)
    
    is_urgent = models.BooleanField(default=False)
    published_date = models.DateField(auto_now_add=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-is_urgent', '-published_date']

    def __str__(self):
        return self.title


class OnlineForm(models.Model):
    """Various government online forms"""
    
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(unique=True, db_index=True)
    
    category = models.CharField(
        max_length=50,
        choices=[
            ('Job Application', 'Job Application'),
            ('Admission', 'Admission Form'),
            ('Certificate', 'Certificate Application'),
            ('License', 'License Application'),
            ('Scholarship', 'Scholarship Application'),
            ('Other', 'Other'),
        ]
    )
    
    organization = models.ForeignKey(Organization, on_delete=models.SET_NULL, null=True, blank=True)
    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True, blank=True)
    
    form_link = models.URLField()
    application_fee = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    
    start_date = models.DateField()
    end_date = models.DateField()
    
    eligibility = models.TextField(blank=True)
    instructions = models.TextField(blank=True)
    
    status = models.CharField(
        max_length=20,
        choices=[
            ('Active', 'Active'),
            ('Closed', 'Closed'),
            ('Extended', 'Extended'),
        ],
        default='Active'
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-start_date']

    def __str__(self):
        return self.name
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.exam_name} - Certificate Verification"


# ============= USER-RELATED MODELS =============

class SavedJob(models.Model):
    """Jobs saved by users for later"""
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='saved_jobs')
    job = models.ForeignKey(JobPosting, on_delete=models.CASCADE)
    saved_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['user', 'job']
        verbose_name_plural = "Saved Jobs"

    def __str__(self):
        return f"{self.user.username} saved {self.job.title}"