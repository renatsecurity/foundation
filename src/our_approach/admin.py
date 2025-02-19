from django.contrib import admin
from .models import OurApproach


@admin.register(OurApproach)
class OurApproachAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {"slug": ("title",)}
