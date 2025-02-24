from django.shortcuts import render, get_object_or_404
from .models import News, PressRelease, Podcast


def news_list(request):
    news = News.objects.all()
    return render(request, 'media_app/blog.html', {'news': news})


def news_detail(request, slug):
    news_item = get_object_or_404(News, slug=slug)
    return render(request, 'media_app/blog-details.html', {'news_item': news_item})


def press_release_list(request):
    press_releases = PressRelease.objects.all()
    return render(request, 'media_app/press_release_list.html', {'press_releases': press_releases})


def press_release_detail(request, slug):
    press_release = get_object_or_404(PressRelease, slug=slug)
    return render(request, 'media_app/press_release_detail.html', {'press_release': press_release})


def podcast_list(request):
    podcasts = Podcast.objects.all()
    return render(request, 'media_app/podcast_list.html', {'podcasts': podcasts})


def podcast_detail(request, slug):
    podcast = get_object_or_404(Podcast, slug=slug)
    return render(request, 'media_app/podcast_detail.html', {'podcast': podcast})
