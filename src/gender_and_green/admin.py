from django.contrib import admin
from .models import Article, TopicCategory


@admin.register(TopicCategory)
class TopicCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'published_date')
    search_fields = ('title', 'author')
    prepopulated_fields = {'slug': ('title',)}
