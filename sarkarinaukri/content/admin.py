# content/admin.py

from django.contrib import admin
from django.utils.html import format_html

from .models import (
    Organization, ExamCategory, State, QualificationLevel,
    JobPosting, ExamResult, AdmitCard, AnswerKey, Syllabus,
    AdmissionForm, CertificateVerification, SavedJob
)


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
        ('Job Details', {
            'fields': ('vacancies', 'job_level', 'qualification_level', 'min_age', 'max_age', 'salary_min', 'salary_max')
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


@admin.register(ExamResult)
class ExamResultAdmin(admin.ModelAdmin):
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
class AdmitCardAdmin(admin.ModelAdmin):
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
class SyllabusAdmin(admin.ModelAdmin):
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