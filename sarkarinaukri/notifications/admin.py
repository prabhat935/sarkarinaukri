# notifications/admin.py

from django.contrib import admin
from .models import UserPreference, NotificationLog, NotificationTemplate, AlertRule


@admin.register(UserPreference)
class UserPreferenceAdmin(admin.ModelAdmin):
    list_display = ('user', 'alert_frequency', 'email_alerts', 'sms_alerts', 'created_at')
    list_filter = ('alert_frequency', 'email_alerts', 'sms_alerts', 'is_verified')
    search_fields = ('user__username', 'user__email', 'phone_number')
    filter_horizontal = ('selected_states', 'selected_categories', 'selected_organizations')


@admin.register(NotificationLog)
class NotificationLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'channel', 'status', 'subject', 'sent_at', 'created_at')
    list_filter = ('channel', 'status', 'created_at')
    search_fields = ('user__username', 'subject', 'message')
    readonly_fields = ('created_at', 'sent_at')


@admin.register(NotificationTemplate)
class NotificationTemplateAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'created_at')
    list_filter = ('is_active', 'created_at')
    search_fields = ('name', 'description')


@admin.register(AlertRule)
class AlertRuleAdmin(admin.ModelAdmin):
    list_display = ('name', 'alert_type', 'state', 'exam_category', 'organization', 'is_active')
    list_filter = ('alert_type', 'is_active', 'state', 'exam_category', 'organization')
    search_fields = ('name', 'description')
    filter_horizontal = ('notify_users',)
