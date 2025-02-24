from django.contrib import admin
from .models import Testimonial


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation', 'region', 'sector', 'rating')
    search_fields = ('name', 'designation', 'region', 'sector')
    list_filter = ('region', 'sector', 'rating')
    prepopulated_fields = {'slug': ('name',)}
