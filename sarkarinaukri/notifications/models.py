# notifications/models.py

from django.db import models
from django.contrib.auth.models import User
from content.models import State, ExamCategory, Organization


class UserPreference(models.Model):
    """User notification preferences and interests"""
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='notification_preference')
    
    # Interests
    selected_states = models.ManyToManyField(State, blank=True, related_name='interested_users')
    selected_categories = models.ManyToManyField(ExamCategory, blank=True, related_name='interested_users')
    selected_organizations = models.ManyToManyField(Organization, blank=True, related_name='interested_users')
    
    # Notification Settings
    email_alerts = models.BooleanField(default=True)
    sms_alerts = models.BooleanField(default=False)
    push_notifications = models.BooleanField(default=False)
    whatsapp_alerts = models.BooleanField(default=False)
    
    # Alert Frequency
    FREQUENCY_CHOICES = [
        ('real-time', 'Real-time'),
        ('daily', 'Daily Digest'),
        ('weekly', 'Weekly Digest'),
    ]
    alert_frequency = models.CharField(
        max_length=20,
        choices=FREQUENCY_CHOICES,
        default='daily'
    )
    
    # Contact info
    phone_number = models.CharField(max_length=15, blank=True)
    
    # Status
    is_verified = models.BooleanField(default=False)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "User Preferences"

    def __str__(self):
        return f"{self.user.username}'s Preferences"


class NotificationLog(models.Model):
    """Track all sent notifications"""
    
    CHANNEL_CHOICES = [
        ('email', 'Email'),
        ('sms', 'SMS'),
        ('push', 'Push Notification'),
        ('whatsapp', 'WhatsApp'),
    ]
    
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('sent', 'Sent'),
        ('failed', 'Failed'),
        ('bounced', 'Bounced'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    channel = models.CharField(max_length=20, choices=CHANNEL_CHOICES)
    
    subject = models.CharField(max_length=200)
    message = models.TextField()
    
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    error_message = models.TextField(blank=True)
    
    sent_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    # Reference
    related_job_id = models.IntegerField(null=True, blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Notification to {self.user.username} via {self.channel}"


class NotificationTemplate(models.Model):
    """Email/SMS templates"""
    
    name = models.CharField(max_length=100, unique=True)
    subject = models.CharField(max_length=200, blank=True)
    body = models.TextField()
    
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class AlertRule(models.Model):
    """Define notification triggers"""
    
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    
    # Trigger conditions
    state = models.ForeignKey(State, on_delete=models.CASCADE, null=True, blank=True)
    exam_category = models.ForeignKey(ExamCategory, on_delete=models.CASCADE, null=True, blank=True)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, null=True, blank=True)
    
    # Alert type
    ALERT_TYPE_CHOICES = [
        ('new_job', 'New Job Posted'),
        ('result_released', 'Result Released'),
        ('admit_card', 'Admit Card Released'),
        ('answer_key', 'Answer Key Released'),
        ('application_closing', 'Application Closing Soon'),
    ]
    alert_type = models.CharField(max_length=50, choices=ALERT_TYPE_CHOICES)
    
    # Notification settings
    notify_users = models.ManyToManyField(User, blank=True)
    
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
