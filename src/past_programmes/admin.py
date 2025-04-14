from django.contrib import admin
from .models import PastProgramme


@admin.register(PastProgramme)
class PastProgrammeAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')
    search_fields = ('title',)
    filter_list = ('title', 'date')
