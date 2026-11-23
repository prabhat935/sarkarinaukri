# content/admin.py

from django.contrib import admin
from django.utils.html import format_html

from .models import (
    Organization, ExamCategory, State, QualificationLevel,
    JobPosting, ExamResult, AdmitCard, AnswerKey, Syllabus,
    AdmissionForm, CertificateVerification, SavedJob
)
from .search_ping import job_url, notify, notify_jobs


class IndexNowAdminMixin:
    """Tell Bing and other IndexNow engines when a page is added, edited or
    removed in the admin. Google's Indexing API only allows job pages, so
    these pages reach Google through the sitemap instead."""
    detail_url_name = None

    def _page_url(self, obj):
        from django.urls import reverse
        from .search_ping import SITE_URL
        return SITE_URL + reverse(self.detail_url_name, args=[obj.pk])

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        notify([self._page_url(obj)], google=False)

    def delete_model(self, request, obj):
        url = self._page_url(obj)
        super().delete_model(request, obj)
        notify([url], google=False)

    def delete_queryset(self, request, queryset):
        urls = [self._page_url(o) for o in queryset]
        super().delete_queryset(request, queryset)
        notify(urls, google=False)


# ============= REFERENCE MODELS =============

@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_featured', 'created_at')
    search_fields = ('name', 'slug')
    list_filter = ('is_featured', 'created_at')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(ExamCategory)
class ExamCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_featured')
    search_fields = ('name', 'slug')
    list_filter = ('is_featured',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'is_featured')
    search_fields = ('name', 'code')
    list_filter = ('is_featured',)


@admin.register(QualificationLevel)
class QualificationLevelAdmin(admin.ModelAdmin):
    list_display = ('level',)
    readonly_fields = ('level',)


# ============= MAIN CONTENT MODELS =============

@admin.register(JobPosting)
class JobPostingAdmin(admin.ModelAdmin):
    list_display = ('title', 'organization', 'state', 'exam_category', 'status', 'days_remaining', 'created_at')
    search_fields = ('title', 'organization__name', 'state__name', 'exam_category__name')
    list_filter = ('status', 'state', 'organization', 'exam_category', 'job_level', 'created_at')
    prepopulated_fields = {'slug': ('title',)}
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'slug', 'description', 'status')
        }),
        ('Organization & Category', {
            'fields': ('organization', 'exam_category', 'state')
        }),
        ('Job Location (for Google job search)', {
            'fields': ('location_street', 'location_city', 'location_region', 'location_postal_code'),
            'description': 'The hiring office as printed in the official notice. Leave blank if the job is across India with no single office.',
        }),
        ('Job Details', {
            'fields': ('year', 'vacancies', 'job_level', 'qualification_level', 'min_age', 'max_age', 'salary_min', 'salary_max')
        }),
        ('Eligibility', {
            'fields': ('eligibility', 'experience_required', 'gender_preference')
        }),
        ('Important Dates', {
            'fields': ('application_start_date', 'application_end_date', 'exam_date', 'interview_date', 'result_date')
        }),
        ('Application', {
            'fields': ('application_link', 'application_fee')
        }),
        ('SEO', {
            'fields': ('meta_description', 'meta_keywords')
        }),
    )
    readonly_fields = ('created_at', 'updated_at')
    date_hierarchy = 'created_at'

    # Tell Google (Indexing API) and Bing (IndexNow) straight away when a job
    # is added, edited or removed, instead of waiting for the next crawl.
    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        notify_jobs([obj])

    def delete_model(self, request, obj):
        url = job_url(obj)
        super().delete_model(request, obj)
        notify([url], deleted=True)

    def delete_queryset(self, request, queryset):
        urls = [job_url(j) for j in queryset]
        super().delete_queryset(request, queryset)
        notify(urls, deleted=True)


@admin.register(ExamResult)
class ExamResultAdmin(IndexNowAdminMixin, admin.ModelAdmin):
    detail_url_name = 'result_detail'
    list_display = ('exam_name', 'organization', 'state', 'exam_year', 'result_date', 'is_official')
    search_fields = ('exam_name', 'organization__name', 'state__name')
    list_filter = ('is_official', 'organization', 'state', 'exam_year', 'result_date')
    prepopulated_fields = {'slug': ('exam_name',)}
    fieldsets = (
        ('Basic Information', {
            'fields': ('exam_name', 'slug', 'description', 'organization', 'exam_category', 'state')
        }),
        ('Result Details', {
            'fields': ('exam_year', 'result_date', 'total_posts', 'selected_candidates', 'is_official')
        }),
        ('Download Links', {
            'fields': ('result_pdf_link', 'merit_list_link', 'cutoff_marks_link')
        }),
        ('SEO', {
            'fields': ('meta_description',)
        }),
    )
    readonly_fields = ('created_at', 'updated_at')


@admin.register(AdmitCard)
class AdmitCardAdmin(IndexNowAdminMixin, admin.ModelAdmin):
    detail_url_name = 'admit_card_detail'
    list_display = ('exam_name', 'organization', 'exam_date', 'admit_card_date')
    search_fields = ('exam_name', 'organization__name')
    list_filter = ('organization', 'state', 'exam_date', 'admit_card_date')
    prepopulated_fields = {'slug': ('exam_name',)}
    fieldsets = (
        ('Basic Information', {
            'fields': ('exam_name', 'slug', 'description', 'organization', 'exam_category', 'state')
        }),
        ('Admit Card Details', {
            'fields': ('exam_date', 'admit_card_date', 'exam_time', 'exam_duration', 'download_link')
        }),
        ('Instructions', {
            'fields': ('instructions',)
        }),
    )
    readonly_fields = ('created_at', 'updated_at')


@admin.register(AnswerKey)
class AnswerKeyAdmin(admin.ModelAdmin):
    list_display = ('exam_name', 'organization', 'exam_year', 'shift_number', 'is_official', 'is_provisional')
    search_fields = ('exam_name', 'organization__name')
    list_filter = ('organization', 'state', 'exam_year', 'is_official', 'is_provisional')
    prepopulated_fields = {'slug': ('exam_name',)}
    fieldsets = (
        ('Basic Information', {
            'fields': ('exam_name', 'slug', 'description', 'organization', 'exam_category', 'state')
        }),
        ('Exam Details', {
            'fields': ('exam_year', 'exam_date', 'shift_number')
        }),
        ('Answer Key Links', {
            'fields': ('question_paper_link', 'answer_key_link', 'solution_pdf_link')
        }),
        ('Status', {
            'fields': ('is_official', 'is_provisional')
        }),
    )
    readonly_fields = ('created_at', 'updated_at')


@admin.register(Syllabus)
class SyllabusAdmin(IndexNowAdminMixin, admin.ModelAdmin):
    detail_url_name = 'syllabus_detail'
    list_display = ('exam_name', 'organization', 'exam_year')
    search_fields = ('exam_name', 'organization__name')
    list_filter = ('organization', 'state', 'exam_year')
    prepopulated_fields = {'slug': ('exam_name',)}
    fieldsets = (
        ('Basic Information', {
            'fields': ('exam_name', 'slug', 'organization', 'exam_category', 'state')
        }),
        ('Syllabus Details', {
            'fields': ('exam_year', 'subjects', 'detailed_syllabus_link')
        }),
        ('Study Material', {
            'fields': ('important_topics', 'previous_papers_link')
        }),
    )
    readonly_fields = ('created_at', 'updated_at')


@admin.register(AdmissionForm)
class AdmissionFormAdmin(admin.ModelAdmin):
    list_display = ('name', 'institution_name', 'form_start_date', 'form_end_date', 'status')
    search_fields = ('name', 'institution_name')
    list_filter = ('status', 'state', 'exam_category', 'form_start_date')
    prepopulated_fields = {'slug': ('name',)}
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'slug', 'institution_name', 'exam_category', 'state')
        }),
        ('Important Dates', {
            'fields': ('form_start_date', 'form_end_date', 'merit_list_date', 'counselling_date')
        }),
        ('Form Details', {
            'fields': ('form_link', 'application_fee', 'eligibility', 'status')
        }),
    )
    readonly_fields = ('created_at', 'updated_at')


@admin.register(CertificateVerification)
class CertificateVerificationAdmin(admin.ModelAdmin):
    list_display = ('exam_name', 'organization', 'year')
    search_fields = ('exam_name', 'organization__name')
    list_filter = ('organization', 'exam_category', 'year')
    prepopulated_fields = {'slug': ('exam_name',)}
    fieldsets = (
        ('Basic Information', {
            'fields': ('exam_name', 'slug', 'organization', 'exam_category', 'year')
        }),
        ('Verification Details', {
            'fields': ('verification_link', 'instructions')
        }),
    )
    readonly_fields = ('created_at', 'updated_at')


@admin.register(SavedJob)
class SavedJobAdmin(admin.ModelAdmin):
    list_display = ('user', 'job_title', 'saved_at')
    search_fields = ('user__username', 'user__email', 'job__title')
    list_filter = ('saved_at',)
    readonly_fields = ('saved_at', 'user', 'job')
    
    def job_title(self, obj):
        return obj.job.title
    job_title.short_description = 'Job Title'