from django.contrib import admin
from .models import AboutUs, CorporateProfile


@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('title', 'last_updated')


@admin.register(CorporateProfile)
class CorporateProfileAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'last_updated')
    prepopulated_fields = {"slug": ("title",)}
