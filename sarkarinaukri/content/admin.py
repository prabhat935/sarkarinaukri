# content/admin.py

from django.contrib import admin

from .models import JobPosting, ExamResult, AdmitCard, Syllabus

@admin.register(JobPosting)
class JobPostingAdmin(admin.ModelAdmin):
    list_display = ('title', 'organization', 'state', 'category', 'created_at')
    search_fields = ('title', 'organization', 'state', 'category')
    list_filter = ('state', 'category', 'created_at')

@admin.register(ExamResult)
class ExamResultAdmin(admin.ModelAdmin):
    list_display = ('exam_name', 'state', 'category', 'result_date', 'created_at')
    search_fields = ('exam_name', 'state', 'category')
    list_filter = ('state', 'category', 'result_date')

@admin.register(AdmitCard)
class AdmitCardAdmin(admin.ModelAdmin):
    list_display = ('exam_name', 'state', 'category', 'exam_date', 'created_at')
    search_fields = ('exam_name', 'state', 'category')
    list_filter = ('state', 'category', 'exam_date')

@admin.register(Syllabus)
class SyllabusAdmin(admin.ModelAdmin):
    list_display = ('exam_name', 'state', 'category', 'created_at')
    search_fields = ('exam_name', 'state', 'category')
    list_filter = ('state', 'category')