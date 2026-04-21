# content/views.py

from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import JobPosting, ExamResult, AdmitCard, Syllabus

class JobListView(ListView):
    model = JobPosting
    template_name = 'content/job_list.html'
    context_object_name = 'jobs'
    paginate_by = 20

class JobDetailView(DetailView):
    model = JobPosting
    template_name = 'content/job_detail.html'
    context_object_name = 'job'

class ResultListView(ListView):
    model = ExamResult
    template_name = 'content/result_list.html'
    context_object_name = 'results'
    paginate_by = 20

class ResultDetailView(DetailView):
    model = ExamResult
    template_name = 'content/result_detail.html'
    context_object_name = 'result'

class AdmitCardListView(ListView):
    model = AdmitCard
    template_name = 'content/admit_card_list.html'
    context_object_name = 'admit_cards'
    paginate_by = 20

class AdmitCardDetailView(DetailView):
    model = AdmitCard
    template_name = 'content/admit_card_detail.html'
    context_object_name = 'admit_card'

class SyllabusListView(ListView):
    model = Syllabus
    template_name = 'content/syllabus_list.html'
    context_object_name = 'syllabi'
    paginate_by = 20

class SyllabusDetailView(DetailView):
    model = Syllabus
    template_name = 'content/syllabus_detail.html'
    context_object_name = 'syllabus'

# Function-based views for simplicity
def job_list(request):
    jobs = JobPosting.objects.all().order_by('-created_at')
    return render(request, 'content/job_list.html', {'jobs': jobs})

def job_detail(request, pk):
    job = get_object_or_404(JobPosting, pk=pk)
    return render(request, 'content/job_detail.html', {'job': job})

def result_list(request):
    results = ExamResult.objects.all().order_by('-created_at')
    return render(request, 'content/result_list.html', {'results': results})

def result_detail(request, pk):
    result = get_object_or_404(ExamResult, pk=pk)
    return render(request, 'content/result_detail.html', {'result': result})

def admit_card_list(request):
    admit_cards = AdmitCard.objects.all().order_by('-created_at')
    return render(request, 'content/admit_card_list.html', {'admit_cards': admit_cards})

def admit_card_detail(request, pk):
    admit_card = get_object_or_404(AdmitCard, pk=pk)
    return render(request, 'content/admit_card_detail.html', {'admit_card': admit_card})

def syllabus_list(request):
    syllabi = Syllabus.objects.all().order_by('-created_at')
    return render(request, 'content/syllabus_list.html', {'syllabi': syllabi})

def syllabus_detail(request, pk):
    syllabus = get_object_or_404(Syllabus, pk=pk)
    return render(request, 'content/syllabus_detail.html', {'syllabus': syllabus})