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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


admin.site.site_header = 'The Engineer Anoka Foundation Admin Panel'
admin.site.site_title = 'The Engineer Anoka Foundation administration'
admin.site.index_title = 'Welcome to The Engineer Anoka Foundation Admin Panel'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    path("accounts/", include("accounts.urls")),
    path('impact/', include('impact.urls')),
    path('mentors/', include('mentor.urls')),
    path('partners/', include('partners.urls')),
    path('events/', include('events.urls')),
    path('careers/', include('careers.urls')),
    path('resources/', include('resources.urls')),
    path('i18n/', include('django.conf.urls.i18n')),
    path("ckeditor5/", include('django_ckeditor_5.urls')),
    path('tinymce/', include('tinymce.urls')),
    path('newsletter/', include('newsletter.urls')),
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
