from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.template.response import TemplateResponse
from django.db.models import Q

from content.models import (
    JobPosting, ExamResult, AdmitCard, AnswerKey,
    Syllabus, BoardExamResult, Scholarship,
    ImportantNotification, OnlineForm, CertificateVerification,
)


def search(request):
    query = request.GET.get("query", "").strip()
    filter_type = request.GET.get("type", "all")
    page_num = request.GET.get("page", 1)

    results = []
    total_count = 0
    type_counts = {}

    if query:
        # Jobs
        job_qs = JobPosting.objects.filter(
            Q(title__icontains=query) |
            Q(organization__name__icontains=query) |
            Q(exam_category__name__icontains=query) |
            Q(eligibility__icontains=query)
        ).select_related("organization", "state", "exam_category").order_by("-created_at")

        # Results
        result_qs = ExamResult.objects.filter(
            Q(exam_name__icontains=query) |
            Q(organization__name__icontains=query)
        ).select_related("organization").order_by("-result_date")

        # Admit Cards
        admit_qs = AdmitCard.objects.filter(
            Q(exam_name__icontains=query) |
            Q(organization__name__icontains=query)
        ).select_related("organization").order_by("-admit_card_date")

        # Answer Keys
        answer_qs = AnswerKey.objects.filter(
            Q(exam_name__icontains=query) |
            Q(organization__name__icontains=query)
        ).select_related("organization").order_by("-publication_date")

        # Syllabus
        syllabus_qs = Syllabus.objects.filter(
            Q(exam_name__icontains=query) |
            Q(organization__name__icontains=query)
        ).select_related("organization").order_by("-created_at")

        # Notifications
        notify_qs = ImportantNotification.objects.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query)
        ).order_by("-published_date")

        type_counts = {
            "jobs":     job_qs.count(),
            "results":  result_qs.count(),
            "admit":    admit_qs.count(),
            "answer":   answer_qs.count(),
            "syllabus": syllabus_qs.count(),
            "notify":   notify_qs.count(),
        }
        total_count = sum(type_counts.values())

        # Build unified result list
        def tag(qs, label, url_prefix, date_field=None):
            out = []
            for obj in qs:
                date_val = getattr(obj, date_field, None) if date_field else None
                name = getattr(obj, "title", None) or getattr(obj, "exam_name", None) or str(obj)
                org = getattr(getattr(obj, "organization", None), "name", None) or ""
                out.append({
                    "type":   label,
                    "name":   name,
                    "org":    org,
                    "date":   date_val,
                    "url":    url_prefix,
                })
            return out

        if filter_type == "jobs":
            combined = tag(job_qs, "jobs", "/content/jobs/", "application_end_date")
        elif filter_type == "results":
            combined = tag(result_qs, "results", "/content/results/", "result_date")
        elif filter_type == "admit":
            combined = tag(admit_qs, "admit", "/content/admit-cards/", "admit_card_date")
        elif filter_type == "answer":
            combined = tag(answer_qs, "answer", "/content/answer-keys/", "publication_date")
        elif filter_type == "syllabus":
            combined = tag(syllabus_qs, "syllabus", "/content/syllabus/", "created_at")
        elif filter_type == "notify":
            combined = tag(notify_qs, "notify", "/content/important-notifications/", "published_date")
        else:
            combined = (
                tag(job_qs[:8],      "jobs",     "/content/jobs/",                    "application_end_date") +
                tag(result_qs[:6],   "results",  "/content/results/",                  "result_date") +
                tag(admit_qs[:6],    "admit",    "/content/admit-cards/",              "admit_card_date") +
                tag(answer_qs[:4],   "answer",   "/content/answer-keys/",              "publication_date") +
                tag(syllabus_qs[:4], "syllabus", "/content/syllabus/",                 "created_at") +
                tag(notify_qs[:4],   "notify",   "/content/important-notifications/",  "published_date")
            )

        paginator = Paginator(combined, 20)
        try:
            results = paginator.page(page_num)
        except PageNotAnInteger:
            results = paginator.page(1)
        except EmptyPage:
            results = paginator.page(paginator.num_pages)
    else:
        paginator = Paginator([], 20)
        results = paginator.page(1)

    return TemplateResponse(
        request,
        "search/search.html",
        {
            "query":        query,
            "filter_type":  filter_type,
            "results":      results,
            "total_count":  total_count,
            "type_counts":  type_counts,
            "is_paginated": results.has_other_pages() if query else False,
            "page_obj":     results,
        },
    )
