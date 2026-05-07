from django.urls import path
from . import views

urlpatterns = [
    path('preferences/', views.preferences, name='notification_preferences'),
    path('save-job/<int:job_id>/', views.save_job, name='save_job'),
]
