from django.shortcuts import render, get_object_or_404
from .models import Career


def career_list(request):
    careers = Career.objects.all().order_by('-posted_date')
    return render(request, 'careers/career_list.html', {'careers': careers})


def career_detail(request, slug):
    career = get_object_or_404(Career, slug=slug)
    return render(request, 'careers/career_detail.html', {'career': career})
