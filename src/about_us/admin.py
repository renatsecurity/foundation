from django.contrib import admin
from .models import MissionVision, CorporateProfile, AboutPartner, AboutMentor, GetInvolved, UpcomingEvent


@admin.register(MissionVision)
class MissionVisionAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'last_updated')
    prepopulated_fields = {"slug": ("title",)}


@admin.register(CorporateProfile)
class CorporateProfileAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'last_updated')
    prepopulated_fields = {"slug": ("title",)}


@admin.register(AboutPartner)
class AboutPartnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'website')
    prepopulated_fields = {"slug": ("name",)}


@admin.register(AboutMentor)
class AboutMentorAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {"slug": ("name",)}


@admin.register(GetInvolved)
class GetInvolvedAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'last_updated')
    prepopulated_fields = {"slug": ("title",)}


@admin.register(UpcomingEvent)
class UpcomingEventAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'date', 'location')
    prepopulated_fields = {"slug": ("title",)}

