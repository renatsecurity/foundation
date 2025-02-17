from django.contrib import admin
from .models import Partner, PartnerGroup


class PartnerInline(admin.TabularInline):
    model = Partner
    extra = 1


@admin.register(PartnerGroup)
class PartnerGroupAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    inlines = [PartnerInline]


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'website', 'group')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}
