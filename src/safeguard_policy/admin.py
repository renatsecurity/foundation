from django.contrib import admin
from .models import SafeguardPolicy


@admin.register(SafeguardPolicy)
class SafeguardPolicyAdmin(admin.ModelAdmin):
    list_display = ('title', 'last_updated')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}
