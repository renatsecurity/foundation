from django.contrib import admin
from .models import Mentor


@admin.register(Mentor)
class MentorAdmin(admin.ModelAdmin):
    list_display = ('name', 'expertise')
    search_fields = ('name', 'expertise')
    prepopulated_fields = {'slug': ('name',)}
