from django.contrib import admin
from .models import Opportunity, OpportunityCategory


@admin.register(OpportunityCategory)
class OpportunityCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Opportunity)
class OpportunityAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'deadline')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}
