from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
from django.template.response import TemplateResponse
from django.urls import reverse

from content.models import (
    AdmitCard, AnswerKey, Article, ExamResult, ImportantNotification, JobPosting, Syllabus,
    written_up_jobs,
)


def _item(obj, kind, url, name, org='', date=None):
    return {'type': kind, 'name': name, 'org': org, 'date': date, 'url': url}


def search(request):
    """Site search over pages with a real write-up only: job posts, results,
    admit cards, syllabus pages and exam guides. Old one-line placeholder
    entries never appear here."""
    query = request.GET.get("query", "").strip()
    filter_type = request.GET.get("type", "all")
    page_num = request.GET.get("page", 1)

    total_count = 0
    type_counts = {}
    combined = []

    if query:
        org_match = Q(organization__name__icontains=query)

        jobs = written_up_jobs(
            JobPosting.objects.filter(
                Q(title__icontains=query) | org_match |
                Q(exam_category__name__icontains=query) | Q(eligibility__icontains=query)
            ).select_related("organization").order_by("-created_at")
        )
        # Open jobs first, then closed ones
        jobs.sort(key=lambda j: (not j.is_open, -(j.created_at.timestamp())))

        results = ExamResult.listed(
            ExamResult.objects.filter(Q(exam_name__icontains=query) | org_match)
            .select_related("organization").order_by("-result_date")
        )
        admits = AdmitCard.listed(
            AdmitCard.objects.filter(Q(exam_name__icontains=query) | org_match)
            .select_related("organization").order_by("-admit_card_date")
        )
        answers = AnswerKey.listed(
            AnswerKey.objects.filter(Q(exam_name__icontains=query) | org_match)
            .select_related("organization").order_by("-publication_date")
        )
        syllabi = Syllabus.listed(
            Syllabus.objects.filter(Q(exam_name__icontains=query) | org_match)
            .select_related("organization").order_by("-created_at")
        )
        guides = list(Article.published().filter(
            Q(title__icontains=query) | Q(excerpt__icontains=query) | Q(content__icontains=query)
        ))
        notices = list(ImportantNotification.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        ).order_by("-published_date"))

        groups = {
            "jobs": [_item(j, "jobs", reverse("job_detail", args=[j.pk]), j.title,
                           j.organization.name if j.organization else "", j.application_end_date) for j in jobs],
            "guides": [_item(a, "guides", reverse("article_detail", args=[a.slug]), a.title,
                             "Exam guide", a.published_date) for a in guides],
            "results": [_item(r, "results", reverse("result_detail", args=[r.pk]), r.display_name,
                              r.organization.name, r.result_date) for r in results],
            "admit": [_item(a, "admit", reverse("admit_card_detail", args=[a.pk]), a.exam_name,
                            a.organization.name, a.admit_card_date) for a in admits],
            "answer": [_item(a, "answer", reverse("answer_key_list"), a.exam_name,
                             a.organization.name, a.publication_date) for a in answers],
            "syllabus": [_item(s, "syllabus", reverse("syllabus_detail", args=[s.pk]), s.exam_name,
                               s.organization.name, None) for s in syllabi],
            "notify": [_item(n, "notify", reverse("important_notifications"), n.title,
                             "", n.published_date) for n in notices],
        }
        type_counts = {k: len(v) for k, v in groups.items()}
        total_count = sum(type_counts.values())

        if filter_type in groups:
            combined = groups[filter_type]
        else:
            filter_type = "all"
            for key in ["jobs", "guides", "results", "admit", "answer", "syllabus", "notify"]:
                combined += groups[key]

    paginator = Paginator(combined, 20)
    try:
        page = paginator.page(page_num)
    except PageNotAnInteger:
        page = paginator.page(1)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)

    return TemplateResponse(
        request,
        "search/search.html",
        {
            "query":        query,
            "filter_type":  filter_type,
            "results":      page,
            "total_count":  total_count,
            "type_counts":  type_counts,
            "is_paginated": page.has_other_pages() if query else False,
            "page_obj":     page,
        },
    )
