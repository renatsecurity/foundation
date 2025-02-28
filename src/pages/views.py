from django.shortcuts import render
from about_us.models import AboutUs
from media_app.models import News
from partners.models import Partner
from .models import Slider, DidYouKnow


def custom_error_404_view(request, exception):
    return render(request, "404.html", {})


def custom_error_500_view(request, exception=None):
    return render(request, "500.html", {})


def home(request):
    about_us = AboutUs.objects.first()
    news = News.objects.filter(is_published=True).order_by('-published_date')[:3]
    partners = Partner.objects.all()
    sliders = Slider.objects.filter(is_visible=True)
    did_you_knows = DidYouKnow.objects.filter(is_visible=True).order_by('-created_on')
    context = {
        'about_us': about_us,
        'news': news,
        'partners': partners,
        'sliders': sliders,
        'did_you_knows': did_you_knows
    }
    return render(request, 'pages/index.html', context)
