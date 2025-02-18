from django.contrib import admin
from .models import Alumni


@admin.register(Alumni)
class AlumniAdmin(admin.ModelAdmin):
    list_display = ('name', 'graduation_year', 'occupation', 'location')
    search_fields = ('name', 'occupation', 'location')
    prepopulated_fields = {'slug': ('name',)}
