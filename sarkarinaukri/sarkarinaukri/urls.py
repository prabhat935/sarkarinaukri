from django.conf import settings
from django.urls import include, path
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.http import HttpResponse

from wagtail.admin import urls as wagtailadmin_urls
from wagtail import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls

from search import views as search_views
from home import views as home_views
from .sitemaps import sitemaps


def robots_txt(request):
    host = request.build_absolute_uri('/').rstrip('/')
    lines = [
        "User-agent: *",
        "Disallow: /django-admin/",
        "Disallow: /admin/",
        "Disallow: /notifications/",
        "Disallow: /search/?*",
        "Allow: /search/",
        "",
        f"Sitemap: {host}/sitemap.xml",
    ]
    return HttpResponse('\n'.join(lines), content_type='text/plain')


def ads_txt(request):
    content = "google.com, pub-2969963906699889, DIRECT, f08c47fec0942fa0\n"
    return HttpResponse(content, content_type='text/plain')



urlpatterns = [
    path("django-admin/", admin.site.urls),
    path("admin/", include(wagtailadmin_urls)),
    path("documents/", include(wagtaildocs_urls)),
    path("search/", search_views.search, name="search"),
    path("content/", include("content.urls")),
    path("notifications/", include("notifications.urls")),

    # SEO
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps},
         name="django.contrib.sitemaps.views.sitemap"),
    path("robots.txt", robots_txt, name="robots_txt"),
    path("ads.txt", ads_txt, name="ads_txt"),

    # Legal and Info Pages
    path("privacy-policy/", home_views.privacy_policy, name="privacy_policy"),
    path("terms-of-service/", home_views.terms_of_service, name="terms_of_service"),
    path("disclaimer/", home_views.disclaimer, name="disclaimer"),
    path("about-us/", home_views.about_us, name="about_us"),
]


if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = urlpatterns + [
    # For anything not caught by a more specific rule above, hand over to
    # Wagtail's page serving mechanism. This should be the last pattern in
    # the list:
    path("", include(wagtail_urls)),
    # Alternatively, if you want Wagtail pages to be served from a subpath
    # of your site, rather than the site root:
    #    path("pages/", include(wagtail_urls)),
]
