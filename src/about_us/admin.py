from django.contrib import admin
from .models import AboutUs, CorporateProfile, MissionAndVision


@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('title', 'youtube_video', 'last_updated')


@admin.register(MissionAndVision)
class MissionAndVisionAdmin(admin.ModelAdmin):
    list_display = ('title', 'last_updated')


@admin.register(CorporateProfile)
class CorporateProfileAdmin(admin.ModelAdmin):
    list_display = ('title', 'last_updated')
