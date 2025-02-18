from django.shortcuts import render, get_object_or_404
from .models import Media


def media_list(request):
    media_items = Media.objects.all().order_by('-published_date')
    return render(request, 'media_app/media_list.html', {'media_items': media_items})


def media_detail(request, slug):
    media = get_object_or_404(Media, slug=slug)
    return render(request, 'media_app/media_detail.html', {'media': media})


def media_type_list(request, media_type):
    media_items = Media.objects.filter(media_type=media_type.replace('-', ' ')).order_by('-published_date')
    return render(request, 'media_app/media_type_list.html', {'media_items': media_items, 'media_type': media_type.replace('-', ' ')})
