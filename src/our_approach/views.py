from django.shortcuts import render, get_object_or_404
from .models import OurApproach


def our_approach_list(request):
    approaches = OurApproach.objects.all()
    return render(request, 'our_approach/our_approach_list.html', {'approaches': approaches})


def our_approach_detail(request, slug):
    approach = get_object_or_404(OurApproach, slug=slug)
    return render(request, 'our_approach/our_approach_detail.html', {'approach': approach})
