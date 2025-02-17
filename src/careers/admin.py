from django.contrib import admin
from .models import Career


@admin.register(Career)
class CareerAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'posted_date', 'deadline')
    search_fields = ('title', 'description', 'requirements')
    prepopulated_fields = {'slug': ('title',)}
