from django.shortcuts import render, get_object_or_404
from .models import AboutUs, CorporateProfile


def about_us(request):
    about = AboutUs.objects.first()
    return render(request, 'about_us/about.html', {'about': about})


def corporate_profile(request):
    profile = CorporateProfile.objects.first()
    return render(request, 'about_us/corporate_profile.html', {'profile': profile})


def corporate_profile_detail(request, slug):
    profile = get_object_or_404(CorporateProfile, slug=slug)
    return render(request, 'about_us/corporate_profile.html', {'profile': profile})
