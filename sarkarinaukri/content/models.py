# content/models.py

from django.db import models
from django.utils import timezone

class JobPosting(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    organization = models.CharField(max_length=100)
    state = models.CharField(max_length=50, blank=True)
    category = models.CharField(max_length=50, blank=True)  # e.g., SSC, UPSC, etc.
    vacancies = models.PositiveIntegerField(default=0)
    application_start_date = models.DateField(null=True, blank=True)
    application_end_date = models.DateField(null=True, blank=True)
    exam_date = models.DateField(null=True, blank=True)
    eligibility = models.TextField(blank=True)
    application_link = models.URLField(blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']

class ExamResult(models.Model):
    exam_name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    state = models.CharField(max_length=50, blank=True)
    category = models.CharField(max_length=50, blank=True)
    result_date = models.DateField(null=True, blank=True)
    download_link = models.URLField(blank=True)
    merit_list = models.TextField(blank=True)  # or file field
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.exam_name

    class Meta:
        ordering = ['-created_at']

class AdmitCard(models.Model):
    exam_name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    state = models.CharField(max_length=50, blank=True)
    category = models.CharField(max_length=50, blank=True)
    exam_date = models.DateField(null=True, blank=True)
    download_link = models.URLField(blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.exam_name

    class Meta:
        ordering = ['-created_at']

class Syllabus(models.Model):
    exam_name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    state = models.CharField(max_length=50, blank=True)
    category = models.CharField(max_length=50, blank=True)
    download_link = models.URLField(blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.exam_name

    class Meta:
        ordering = ['-created_at']