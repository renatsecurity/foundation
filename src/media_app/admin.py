from django.contrib import admin
from .models import News, PressRelease, Podcast

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_date')
    prepopulated_fields = {'slug': ('title',)}

@admin.register(PressRelease)
class PressReleaseAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_date')
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Podcast)
class PodcastAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_date')
    prepopulated_fields = {'slug': ('title',)}
