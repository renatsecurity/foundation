from django.contrib import admin
from .models import Research, ResearchCategory


@admin.register(ResearchCategory)
class ResearchCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Research)
class ResearchAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_date', 'category')
    search_fields = ('title', 'author')
    prepopulated_fields = {'slug': ('title',)}
