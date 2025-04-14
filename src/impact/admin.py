from django.contrib import admin
from .models import Impact, State, Category


@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ('name', 'impact_value')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'impact_value')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Impact)
class ImpactAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}
