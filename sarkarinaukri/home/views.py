"""
Views for legal and informational pages
"""
from django.shortcuts import render
from django.views.decorators.http import require_http_methods


@require_http_methods(["GET"])
def privacy_policy(request):
    """Render privacy policy page"""
    return render(request, 'home/privacy_policy.html')


@require_http_methods(["GET"])
def terms_of_service(request):
    """Render terms of service page"""
    return render(request, 'home/terms_of_service.html')


@require_http_methods(["GET"])
def disclaimer(request):
    """Render disclaimer page"""
    return render(request, 'home/disclaimer.html')


@require_http_methods(["GET"])
def about_us(request):
    """Render about us page"""
    return render(request, 'home/about_us.html')


@require_http_methods(["GET"])
def contact(request):
    """Contact page: how to reach the site and what we can help with"""
    return render(request, 'home/contact.html')


@require_http_methods(["GET"])
def about_authors(request):
    """Render about authors page - E-E-A-T credibility signal"""
    return render(request, 'home/about_authors.html')


@require_http_methods(["GET"])
def age_calculator(request):
    """Age eligibility calculator; the calculation runs in the browser"""
    return render(request, 'home/age_calculator.html')


@require_http_methods(["GET"])
def photo_resizer(request):
    """Photo and signature resizer for exam forms; runs in the browser"""
    return render(request, 'home/tools/photo_resizer.html')


@require_http_methods(["GET"])
def typing_test(request):
    """SSC typing test practice; runs in the browser"""
    return render(request, 'home/tools/typing_test.html')


@require_http_methods(["GET"])
def score_calculator(request):
    """Exam score calculator with negative marking; runs in the browser"""
    return render(request, 'home/tools/score_calculator.html')


@require_http_methods(["GET"])
def cgpa_converter(request):
    """CGPA to percentage converter; runs in the browser"""
    return render(request, 'home/tools/cgpa_converter.html')


@require_http_methods(["GET"])
def exam_countdown(request):
    """Upcoming exam dates and application last dates from the site's own posts"""
    import datetime
    from content.models import AdmitCard, JobPosting, written_up_jobs

    today = datetime.date.today()
    jobs = written_up_jobs(JobPosting.objects.select_related('organization'))
    events = []
    for j in jobs:
        if j.exam_date and j.exam_date >= today:
            events.append({'date': j.exam_date, 'kind': 'exam', 'name': j.short_title,
                           'org': j.organization.name, 'url': f'/content/job/{j.pk}/'})
    for a in AdmitCard.listed(AdmitCard.objects.filter(exam_date__gte=today).select_related('organization')):
        events.append({'date': a.exam_date, 'kind': 'exam', 'name': a.exam_name,
                       'org': a.organization.name, 'url': f'/content/admit-card/{a.pk}/'})
    deadlines = sorted(
        ({'date': j.application_end_date, 'kind': 'apply', 'name': j.short_title,
          'org': j.organization.name, 'url': f'/content/job/{j.pk}/'}
         for j in jobs if j.is_open and j.application_end_date),
        key=lambda e: e['date'])
    events.sort(key=lambda e: e['date'])
    for e in events + deadlines:
        e['days'] = (e['date'] - today).days
    return render(request, 'home/tools/exam_countdown.html',
                  {'exams': events, 'deadlines': deadlines, 'today': today})


@require_http_methods(["GET"])
def salary_calculator(request):
    """7th CPC in-hand salary calculator; runs in the browser"""
    return render(request, 'home/tools/salary_calculator.html')
