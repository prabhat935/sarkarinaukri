# content/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('jobs/', views.JobListView.as_view(), name='job_list'),
    path('results/', views.ResultListView.as_view(), name='result_list'),
    path('admit-cards/', views.AdmitCardListView.as_view(), name='admit_card_list'),
    path('syllabus/', views.SyllabusListView.as_view(), name='syllabus_list'),
    path('job/<int:pk>/', views.JobDetailView.as_view(), name='job_detail'),
    path('result/<int:pk>/', views.ResultDetailView.as_view(), name='result_detail'),
    path('admit-card/<int:pk>/', views.AdmitCardDetailView.as_view(), name='admit_card_detail'),
    path('syllabus/<int:pk>/', views.SyllabusDetailView.as_view(), name='syllabus_detail'),
    
    # New functionalities
    path('board-results/', views.board_results, name='board_results'),
    path('scholarships/', views.scholarships, name='scholarships'),
    path('important-notifications/', views.important_notifications, name='important_notifications'),
    path('online-forms/', views.online_forms, name='online_forms'),
    path('certificate-verification/', views.certificate_verification, name='certificate_verification'),
]