from django.http import HttpResponsePermanentRedirect

CANONICAL_HOST = 'www.sarkarinaukriresult.online'
BARE_HOST = 'sarkarinaukriresult.online'


class CanonicalHostMiddleware:
    """Send visitors and crawlers on the bare domain to the www address with a
    301, so the site exists at one address only. Other hosts (Railway's own
    domain, health checks) are left alone."""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        host = request.get_host().split(':')[0].lower()
        if host == BARE_HOST:
            return HttpResponsePermanentRedirect(f'https://{CANONICAL_HOST}{request.get_full_path()}')
        return self.get_response(request)
