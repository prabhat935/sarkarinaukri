# content/views.py

from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.db.models import Q
from django_filters import FilterSet, CharFilter, ChoiceFilter, DateFromToRangeFilter
import django_filters
from .models import (
    JobPosting, ExamResult, AdmitCard, Syllabus, AnswerKey,
    Organization, ExamCategory, State, AdmissionForm, CertificateVerification,
    BoardExamResult, Scholarship, ImportantNotification, OnlineForm
)


# ============= FILTER CLASSES =============

class JobPostingFilter(django_filters.FilterSet):
    """Advanced filtering for job postings"""
    title = django_filters.CharFilter(
        lookup_expr='icontains',
        label='Job Title'
    )
    organization = django_filters.ModelChoiceFilter(
        queryset=Organization.objects.all(),
        label='Organization'
    )
    state = django_filters.ModelChoiceFilter(
        queryset=State.objects.filter(is_featured=True),
        label='State'
    )
    exam_category = django_filters.ModelChoiceFilter(
        queryset=ExamCategory.objects.all(),
        label='Category'
    )
    status = django_filters.ChoiceFilter(
        choices=JobPosting._meta.get_field('status').choices
    )
    job_level = django_filters.ChoiceFilter(
        choices=JobPosting._meta.get_field('job_level').choices
    )
    application_end_date = django_filters.DateFromToRangeFilter(
        label='Application Deadline'
    )

    class Meta:
        model = JobPosting
        fields = ['title', 'organization', 'state', 'exam_category', 'status', 'job_level']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Make filters not required
        for field in self.filters:
            self.filters[field].extra['required'] = False


# ============= VIEW CLASSES =============

class JobListView(ListView):
    """Job listings with advanced filtering"""
    model = JobPosting
    template_name = 'content/job_list.html'
    context_object_name = 'jobs'
    paginate_by = 20

    def get_queryset(self):
        queryset = JobPosting.objects.select_related(
            'organization', 'state', 'exam_category'
        ).order_by('-year', '-application_end_date', '-created_at')
        
        # Apply filters
        filterset = JobPostingFilter(self.request.GET, queryset=queryset)
        return filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = JobPostingFilter(self.request.GET)
        
        # Add filter options
        context['organizations'] = Organization.objects.filter(is_featured=True)
        context['states'] = State.objects.filter(is_featured=True)
        context['categories'] = ExamCategory.objects.filter(is_featured=True)
        
        return context


class JobDetailView(DetailView):
    """Job detail page with related jobs"""
    model = JobPosting
    template_name = 'content/job_detail.html'
    context_object_name = 'job'
    slug_field = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        job = self.get_object()
        
        # Show related jobs from same organization
        context['related_jobs'] = JobPosting.objects.filter(
            organization=job.organization,
            status='Active'
        ).exclude(pk=job.pk)[:5]
        
        # Check if user has saved this job
        if self.request.user.is_authenticated:
            from .models import SavedJob
            context['is_saved'] = SavedJob.objects.filter(
                user=self.request.user,
                job=job
            ).exists()
        
        return context


class ResultListView(ListView):
    """Results listing with year and organization filtering"""
    model = ExamResult
    template_name = 'content/result_list.html'
    context_object_name = 'results'
    paginate_by = 20

    def get_queryset(self):
        queryset = ExamResult.objects.select_related(
            'organization', 'state', 'exam_category'
        ).order_by('-exam_year', '-result_date')
        
        # Filter by organization
        org_id = self.request.GET.get('organization')
        if org_id:
            queryset = queryset.filter(organization_id=org_id)
        
        # Filter by state
        state_id = self.request.GET.get('state')
        if state_id:
            queryset = queryset.filter(state_id=state_id)
        
        # Filter by year
        year = self.request.GET.get('year')
        if year:
            queryset = queryset.filter(exam_year=year)
        
        # Search by exam name
        search = self.request.GET.get('search')
        if search:
            queryset = queryset.filter(exam_name__icontains=search)
        
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['organizations'] = Organization.objects.filter(is_featured=True)
        context['states'] = State.objects.filter(is_featured=True)
        
        # Get available years
        years = ExamResult.objects.values_list('exam_year', flat=True).distinct().order_by('-exam_year')
        context['years'] = years[:10]  # Last 10 years
        
        # Preserve search params
        context['selected_org'] = self.request.GET.get('organization')
        context['selected_state'] = self.request.GET.get('state')
        context['selected_year'] = self.request.GET.get('year')
        context['search_query'] = self.request.GET.get('search')
        
        return context


class ResultDetailView(DetailView):
    """Result detail page"""
    model = ExamResult
    template_name = 'content/result_detail.html'
    context_object_name = 'result'
    slug_field = 'slug'


class AdmitCardListView(ListView):
    """Admit cards listing"""
    model = AdmitCard
    template_name = 'content/admit_card_list.html'
    context_object_name = 'admit_cards'
    paginate_by = 20

    def get_queryset(self):
        queryset = AdmitCard.objects.select_related(
            'organization', 'state', 'exam_category'
        ).order_by('-admit_card_date')
        
        # Filter by organization
        org_id = self.request.GET.get('organization')
        if org_id:
            queryset = queryset.filter(organization_id=org_id)
        
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['organizations'] = Organization.objects.filter(is_featured=True)
        return context


class AdmitCardDetailView(DetailView):
    """Admit card detail page"""
    model = AdmitCard
    template_name = 'content/admit_card_detail.html'
    context_object_name = 'admit_card'
    slug_field = 'slug'


class AnswerKeyListView(ListView):
    """Answer keys listing"""
    model = AnswerKey
    template_name = 'content/answer_key_list.html'
    context_object_name = 'answer_keys'
    paginate_by = 20

    def get_queryset(self):
        return AnswerKey.objects.select_related(
            'organization', 'state', 'exam_category'
        ).order_by('-exam_date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['organizations'] = Organization.objects.filter(is_featured=True)
        return context


class SyllabusListView(ListView):
    """Syllabus listing"""
    model = Syllabus
    template_name = 'content/syllabus_list.html'
    context_object_name = 'syllabi'
    paginate_by = 20

    def get_queryset(self):
        return Syllabus.objects.select_related(
            'organization', 'state', 'exam_category'
        ).order_by('-exam_year')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['organizations'] = Organization.objects.filter(is_featured=True)
        return context


class SyllabusDetailView(DetailView):
    """Syllabus detail page"""
    model = Syllabus
    template_name = 'content/syllabus_detail.html'
    context_object_name = 'syllabus'
    slug_field = 'slug'

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


# ============= NEW FUNCTIONALITY VIEWS =============

class BoardExamResultListView(ListView):
    """Board exam results listing"""
    model = BoardExamResult
    template_name = 'content/board_results.html'
    context_object_name = 'board_results'
    paginate_by = 20

    def get_queryset(self):
        queryset = BoardExamResult.objects.all().order_by('-result_date')
        
        # Filter by board
        board = self.request.GET.get('board')
        if board:
            queryset = queryset.filter(board=board)
        
        # Filter by exam type
        exam_type = self.request.GET.get('exam_type')
        if exam_type:
            queryset = queryset.filter(exam_type=exam_type)
        
        # Filter by year
        year = self.request.GET.get('year')
        if year:
            queryset = queryset.filter(year=year)
        
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['boards'] = BoardExamResult.BOARD_CHOICES
        context['exam_types'] = BoardExamResult._meta.get_field('exam_type').choices
        
        # Get available years
        years = BoardExamResult.objects.values_list('year', flat=True).distinct().order_by('-year')
        context['years'] = years[:10]
        
        return context


class ScholarshipListView(ListView):
    """Scholarships listing"""
    model = Scholarship
    template_name = 'content/scholarships.html'
    context_object_name = 'scholarships'
    paginate_by = 20

    def get_queryset(self):
        queryset = Scholarship.objects.filter(status='Open').order_by('-application_end_date')
        
        # Filter by state
        state_id = self.request.GET.get('state')
        if state_id:
            queryset = queryset.filter(state_id=state_id)
        
        # Filter by category
        category = self.request.GET.get('category')
        if category:
            queryset = queryset.filter(category=category)
        
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['states'] = State.objects.filter(is_featured=True)
        context['categories'] = Scholarship._meta.get_field('category').choices
        return context


class ImportantNotificationListView(ListView):
    """Important notifications listing"""
    model = ImportantNotification
    template_name = 'content/important_notifications.html'
    context_object_name = 'notifications'
    paginate_by = 20

    def get_queryset(self):
        queryset = ImportantNotification.objects.all().order_by('-is_urgent', '-published_date')
        
        # Filter by category
        category = self.request.GET.get('category')
        if category:
            queryset = queryset.filter(category=category)
        
        # Filter by state
        state_id = self.request.GET.get('state')
        if state_id:
            queryset = queryset.filter(state_id=state_id)
        
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = ImportantNotification._meta.get_field('category').choices
        context['states'] = State.objects.filter(is_featured=True)
        return context


class OnlineFormListView(ListView):
    """Online forms listing"""
    model = OnlineForm
    template_name = 'content/online_forms.html'
    context_object_name = 'forms'
    paginate_by = 20

    def get_queryset(self):
        queryset = OnlineForm.objects.filter(status='Active').order_by('-start_date')
        
        # Filter by category
        category = self.request.GET.get('category')
        if category:
            queryset = queryset.filter(category=category)
        
        # Filter by state
        state_id = self.request.GET.get('state')
        if state_id:
            queryset = queryset.filter(state_id=state_id)
        
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = OnlineForm._meta.get_field('category').choices
        context['states'] = State.objects.filter(is_featured=True)
        return context


class CertificateVerificationListView(ListView):
    """Certificate verification listing"""
    model = CertificateVerification
    template_name = 'content/certificate_verification.html'
    context_object_name = 'verifications'
    paginate_by = 20

    def get_queryset(self):
        queryset = CertificateVerification.objects.select_related(
            'organization', 'exam_category'
        ).order_by('-created_at')
        
        # Filter by organization
        org_id = self.request.GET.get('organization')
        if org_id:
            queryset = queryset.filter(organization_id=org_id)
        
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['organizations'] = Organization.objects.filter(is_featured=True)
        return context


# Function-based views for new features
def board_results(request):
    """Board exam results page"""
    view = BoardExamResultListView.as_view()
    return view(request)

def scholarships(request):
    """Scholarships page"""
    view = ScholarshipListView.as_view()
    return view(request)

def important_notifications(request):
    """Important notifications page"""
    view = ImportantNotificationListView.as_view()
    return view(request)

def online_forms(request):
    """Online forms page"""
    view = OnlineFormListView.as_view()
    return view(request)

def certificate_verification(request):
    """Certificate verification page"""
    view = CertificateVerificationListView.as_view()
    return view(request)