from django.shortcuts import render, get_object_or_404
from .models import Impact


def impact_list(request):
    impacts = Impact.objects.all().order_by('-date')
    return render(request, 'impact/impact_list.html', {'impacts': impacts})


def impact_detail(request, slug):
    impact = get_object_or_404(Impact, slug=slug)
    return render(request, 'impact/impact_detail.html', {'impact': impact})
