# content/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('jobs/', views.job_list, name='job_list'),
    path('results/', views.result_list, name='result_list'),
    path('admit-cards/', views.admit_card_list, name='admit_card_list'),
    path('syllabus/', views.syllabus_list, name='syllabus_list'),
    path('job/<int:pk>/', views.job_detail, name='job_detail'),
    path('result/<int:pk>/', views.result_detail, name='result_detail'),
    path('admit-card/<int:pk>/', views.admit_card_detail, name='admit_card_detail'),
    path('syllabus/<int:pk>/', views.syllabus_detail, name='syllabus_detail'),
]