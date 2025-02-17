from django.contrib import admin
from .models import Impact


@admin.register(Impact)
class ImpactAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}
