"""Pick exam guides that a job, result or admit card post refers to, so the
page can link to them ("see our guide to the EWS certificate")."""
import re

# (pattern found in the post's text, guide slug)
GUIDE_TOPICS = [
    (r'\bEWS\b', 'ews-certificate-central-government-jobs'),
    (r'\bOBC\b|non-creamy', 'obc-non-creamy-layer-certificate-central-jobs'),
    (r'negative marking|wrong answer', 'negative-marking-when-to-guess'),
    (r'document verification|original certificates', 'document-verification-government-exams-checklist'),
    (r'ex-servicem', 'ex-servicemen-age-relaxation-calculation'),
    (r'age relaxation|relaxation in (?:the )?upper age', 'age-relaxation-government-jobs-2026'),
    (r'\bIBPS\b|\bSBI\b', 'ibps-po-vs-sbi-po-comparison'),
    (r'typing|skill test', 'ssc-typing-skill-test-preparation'),
    (r'admit card|call letter', 'how-to-download-admit-cards-online'),
    (r'answer key', 'answer-key-calculate-score-raise-objection'),
    (r'\bpay level\b', '7th-pay-commission-in-hand-salary-level-4-to-7'),
]


def related_guides(*texts, limit=4):
    from .models import Article
    text = ' '.join(t or '' for t in texts)
    slugs = []
    for pattern, slug in GUIDE_TOPICS:
        if slug not in slugs and re.search(pattern, text, re.I):
            slugs.append(slug)
    if not slugs:
        return []
    found = {a.slug: a for a in Article.published().filter(slug__in=slugs)}
    return [found[s] for s in slugs if s in found][:limit]
