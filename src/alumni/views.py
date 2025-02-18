from django.shortcuts import render, get_object_or_404
from .models import Alumni

def alumni_list(request):
    alumni_members = Alumni.objects.all().order_by('-graduation_year')
    return render(request, 'alumni/alumni_list.html', {'alumni_members': alumni_members})

def alumni_detail(request, slug):
    alumni = get_object_or_404(Alumni, slug=slug)
    return render(request, 'alumni/alumni_detail.html', {'alumni': alumni})