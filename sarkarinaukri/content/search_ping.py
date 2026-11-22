"""
Tell search engines about new or changed job pages as soon as they change.

- IndexNow (Bing, Yandex and others): free, no account. The key below is
  public by design and is served at /<key>.txt to prove we own the site.
- Google Indexing API: Google only accepts it for pages with JobPosting
  structured data, so we use it for job pages only. It needs a service
  account key in the GOOGLE_INDEXING_CREDENTIALS environment variable (the
  whole JSON file as one value), and that service account must be added as an
  Owner of the site in Search Console.

Pings are sent only in production (DEBUG off) unless force=True, and errors
are logged, never raised, so a search-engine outage can never break a save.
"""
import json
import logging
import os
import threading

from django.conf import settings
from django.urls import reverse

logger = logging.getLogger(__name__)

SITE_URL = 'https://www.sarkarinaukriresult.online'
SITE_HOST = 'www.sarkarinaukriresult.online'
INDEXNOW_KEY = '63e143ebdef0518b3d0f44b8c23a897f'
INDEXNOW_ENDPOINT = 'https://api.indexnow.org/indexnow'
GOOGLE_ENDPOINT = 'https://indexing.googleapis.com/v3/urlNotifications:publish'
GOOGLE_SCOPE = 'https://www.googleapis.com/auth/indexing'
TIMEOUT = 15


def job_url(job_or_pk):
    pk = getattr(job_or_pk, 'pk', job_or_pk)
    return SITE_URL + reverse('job_detail', args=[pk])


def _enabled(force):
    return force or not settings.DEBUG


def ping_indexnow(urls):
    import requests
    resp = requests.post(
        INDEXNOW_ENDPOINT,
        json={
            'host': SITE_HOST,
            'key': INDEXNOW_KEY,
            'keyLocation': f'{SITE_URL}/{INDEXNOW_KEY}.txt',
            'urlList': list(urls),
        },
        timeout=TIMEOUT,
    )
    # 200 = accepted, 202 = accepted and key check pending
    return resp.status_code


def _google_session():
    raw = (os.environ.get('GOOGLE_INDEXING_CREDENTIALS')
           or os.environ.get('GOOGLE_INDEXING_CREDENTIAL', '')).strip()
    if not raw:
        return None
    from google.oauth2 import service_account
    from google.auth.transport.requests import AuthorizedSession
    creds = service_account.Credentials.from_service_account_info(
        json.loads(raw), scopes=[GOOGLE_SCOPE]
    )
    return AuthorizedSession(creds)


def ping_google(urls, deleted=False):
    session = _google_session()
    if session is None:
        return {'skipped': 'GOOGLE_INDEXING_CREDENTIALS not set'}
    action = 'URL_DELETED' if deleted else 'URL_UPDATED'
    results = {}
    for url in urls:
        resp = session.post(GOOGLE_ENDPOINT, json={'url': url, 'type': action}, timeout=TIMEOUT)
        results[url] = resp.status_code
        if resp.status_code != 200:
            logger.warning('Google Indexing API %s for %s: %s', resp.status_code, url, resp.text[:300])
    return results


def notify(urls, google=True, deleted=False, force=False, background=True):
    """Ping IndexNow (and Google for job pages). Returns a summary dict when
    run in the foreground; in the background it returns None immediately."""
    urls = [u for u in urls if u]
    if not urls or not _enabled(force):
        return None

    def run():
        summary = {}
        try:
            summary['indexnow'] = ping_indexnow(urls)
        except Exception as exc:  # network errors must never break a save
            logger.warning('IndexNow ping failed: %s', exc)
            summary['indexnow'] = f'error: {exc}'
        if google:
            try:
                summary['google'] = ping_google(urls, deleted=deleted)
            except Exception as exc:
                logger.warning('Google Indexing API ping failed: %s', exc)
                summary['google'] = f'error: {exc}'
        logger.warning('Search ping %s: %s', urls, summary)
        return summary

    if background:
        threading.Thread(target=run, daemon=True).start()
        return None
    return run()


def notify_jobs(jobs, deleted=False, force=False, background=True):
    return notify([job_url(j) for j in jobs], google=True, deleted=deleted,
                  force=force, background=background)
