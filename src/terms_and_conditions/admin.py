from django.contrib import admin
from .models import TermsAndConditions


@admin.register(TermsAndConditions)
class TermsAndConditionsAdmin(admin.ModelAdmin):
    list_display = ('title', 'last_updated')
    search_fields = ('title',)
