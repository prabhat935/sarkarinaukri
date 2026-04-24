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
