"""
URL configuration for enganoka project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib.sitemaps.views import sitemap
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .sitemaps import (
    NewsModelSitemap, PressReleaseModelSitemap, StaticViewSitemap,
    ResourceModelSitemap, ResearchModelSitemap, PastProgrammeModelSitemap,
    ImpactModelSitemap, ArticleModelSitemap, OpportunityModelSitemap,
    EventModelSitemap, CareerModelSitemap, PodcastModelSitemap
)
from .robots import robots_txt


admin.site.site_header = 'Michael Anoka Foundation (MAF) Admin Panel'
admin.site.site_title = 'Michael Anoka Foundation (MAF) administration'
admin.site.index_title = 'Welcome to The Michael Anoka Foundation (MAF) Admin Panel'


sitemaps = {
    'news': NewsModelSitemap,
    'press-release': PressReleaseModelSitemap,
    'resources': ResourceModelSitemap,
    'reseaches': ResearchModelSitemap,
    'past-programmes': PastProgrammeModelSitemap,
    'impacts': ImpactModelSitemap,
    'articles': ArticleModelSitemap,
    'opportunities': OpportunityModelSitemap,
    'events': EventModelSitemap,
    'careers': CareerModelSitemap,
    'podcasts': PodcastModelSitemap,
    'static': StaticViewSitemap,
}

handler404 = 'pages.views.custom_error_404_view'
handler500 = 'pages.views.custom_error_500_view'

urlpatterns = [
    path('aaadmin@123/', admin.site.urls),
    path('', include('pages.urls')),
    path("accounts/", include("accounts.urls")),
    path('impact/', include('impact.urls')),
    path('mentors/', include('mentor.urls')),
    path('partners/', include('partners.urls')),
    path('events/', include('events.urls')),
    path('careers/', include('careers.urls')),
    path('gender-and-green/', include('gender_and_green.urls')),
    path('get_involved/', include('get_involved.urls')),
    path('safeguard-policy/', include('safeguard_policy.urls')),
    path('privacy-policy/', include('privacy_policy.urls')),
    path('terms-and-conditions/', include('terms_and_conditions.urls')),
    path('testimonials/', include('testimonials.urls')),
    path('about-us/', include('about_us.urls')),
    path('research/', include('research.urls')),
    path('resources/', include('resources.urls')),
    path('media_urls/', include('media_app.urls')),
    path('our-approach/', include('our_approach.urls')),
    path('past_programmes/', include('past_programmes.urls')),
    path('alumni/', include('alumni.urls')),
    path('faqs/', include('faqs.urls')),
    path('i18n/', include('django.conf.urls.i18n')),
    path("ckeditor5/", include('django_ckeditor_5.urls')),
    path('tinymce/', include('tinymce.urls')),
    path('newsletter/', include('newsletter.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
    path('robots.txt', robots_txt, name='robots_txt'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL,
        document_root=settings.STATIC_ROOT
    )
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
