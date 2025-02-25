from django.contrib import admin
from .models import News, PressRelease, Podcast, Category, Comment

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'published_date')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'content')
    list_filter = ('category', 'tags', 'published_date')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'news', 'created_at')
    search_fields = ('content', 'name', 'email')
    list_filter = ('is_approved', 'created_at')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(is_approved=True)
        self.message_user(request, "Selected comments have been approved.")
    approve_comments.short_description = "Approve selected comments"


@admin.register(PressRelease)
class PressReleaseAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_date')
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Podcast)
class PodcastAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_date')
    prepopulated_fields = {'slug': ('title',)}
