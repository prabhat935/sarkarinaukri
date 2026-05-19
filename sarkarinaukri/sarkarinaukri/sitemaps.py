"""
Dynamic XML sitemaps for all content types.
Regenerated on every Google/Bing fetch — always reflects current data.
"""
from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from content.models import (
    JobPosting, ExamResult, AdmitCard, Syllabus,
    AnswerKey, ImportantNotification, Article,
)


class StaticPagesSitemap(Sitemap):
    """Home page, list pages, and legal pages."""
    changefreq = 'daily'

    def items(self):
        return [
            ('article_list',              0.9),
            ('job_list',                  1.0),
            ('result_list',               0.9),
            ('admit_card_list',           0.9),
            ('answer_key_list',           0.8),
            ('syllabus_list',             0.8),
            ('board_results',             0.8),
            ('scholarships',              0.7),
            ('important_notifications',   0.8),
            ('online_forms',              0.7),
            ('certificate_verification',  0.6),
            ('search',                    0.5),
            ('about_us',                  0.4),
            ('privacy_policy',            0.3),
            ('terms_of_service',          0.3),
            ('disclaimer',                0.3),
        ]

    def location(self, item):
        url_name, _ = item
        return reverse(url_name)

    def priority(self, item):
        _, prio = item
        return prio


class JobPostingSitemap(Sitemap):
    """Active job postings — high priority, checked weekly."""
    changefreq = 'weekly'
    priority = 0.8

    def items(self):
        return JobPosting.objects.filter(
            status='Active'
        ).order_by('-created_at')

    def location(self, obj):
        return reverse('job_detail', args=[obj.pk])

    def lastmod(self, obj):
        return obj.updated_at


class ClosedJobSitemap(Sitemap):
    """Closed/expired jobs — kept for result-seekers, lower priority."""
    changefreq = 'monthly'
    priority = 0.4

    def items(self):
        return JobPosting.objects.exclude(
            status='Active'
        ).order_by('-updated_at')[:500]

    def location(self, obj):
        return reverse('job_detail', args=[obj.pk])

    def lastmod(self, obj):
        return obj.updated_at


class ExamResultSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.7

    def items(self):
        return ExamResult.objects.all().order_by('-result_date')

    def location(self, obj):
        return reverse('result_detail', args=[obj.pk])

    def lastmod(self, obj):
        return obj.updated_at


class AdmitCardSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.8

    def items(self):
        return AdmitCard.objects.all().order_by('-admit_card_date')

    def location(self, obj):
        return reverse('admit_card_detail', args=[obj.pk])

    def lastmod(self, obj):
        return obj.updated_at


class SyllabusSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.6

    def items(self):
        return Syllabus.objects.all().order_by('-exam_year')

    def location(self, obj):
        return reverse('syllabus_detail', args=[obj.pk])

    def lastmod(self, obj):
        return obj.updated_at


class ArticleSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.8

    def items(self):
        return Article.objects.all()

    def location(self, obj):
        return reverse('article_detail', args=[obj.slug])

    def lastmod(self, obj):
        return obj.updated_at


# Collected for use in urls.py
sitemaps = {
    'static':       StaticPagesSitemap,
    'articles':     ArticleSitemap,
    'jobs':         JobPostingSitemap,
    'jobs-closed':  ClosedJobSitemap,
    'results':      ExamResultSitemap,
    'admit-cards':  AdmitCardSitemap,
    'syllabus':     SyllabusSitemap,
}
