# content/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('jobs/', views.JobListView.as_view(), name='job_list'),
    path('results/', views.ResultListView.as_view(), name='result_list'),
    path('admit-cards/', views.AdmitCardListView.as_view(), name='admit_card_list'),
    path('answer-keys/', views.AnswerKeyListView.as_view(), name='answer_key_list'),
    path('syllabus/', views.SyllabusListView.as_view(), name='syllabus_list'),
    path('board-results/', views.BoardExamResultListView.as_view(), name='board_results'),
    path('scholarships/', views.ScholarshipListView.as_view(), name='scholarships'),
    path('important-notifications/', views.ImportantNotificationListView.as_view(), name='important_notifications'),
    path('online-forms/', views.OnlineFormListView.as_view(), name='online_forms'),
    path('certificate-verification/', views.CertificateVerificationListView.as_view(), name='certificate_verification'),
    path('job/<int:pk>/', views.JobDetailView.as_view(), name='job_detail'),
    path('result/<int:pk>/', views.ResultDetailView.as_view(), name='result_detail'),
    path('admit-card/<int:pk>/', views.AdmitCardDetailView.as_view(), name='admit_card_detail'),
    path('syllabus/<int:pk>/', views.SyllabusDetailView.as_view(), name='syllabus_detail'),
]