from django.contrib import admin
from .models import Slider, DidYouKnow


class SliderAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_visible', 'link')
    list_editable = ('is_visible', 'link')
    search_fields = ('title', 'description')
    list_filter = ('is_visible',)
    ordering = ('-created_on',)


class DidYouKnowAdmin(admin.ModelAdmin):
    list_display = ('description', 'is_visible', 'background_color')
    list_editable = ('is_visible', 'background_color')
    search_fields = ('description', 'background_color')
    list_filter = ('is_visible',)
    ordering = ('-created_on',)


admin.site.register(Slider, SliderAdmin)
admin.site.register(DidYouKnow, DidYouKnowAdmin)
