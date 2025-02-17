from django.shortcuts import render, get_object_or_404
from .models import Event


def event_list(request):
    events = Event.objects.all().order_by('-date')
    return render(request, 'events/event_list.html', {'events': events})


def event_detail(request, slug):
    event = get_object_or_404(Event, slug=slug)
    return render(request, 'events/event_detail.html', {'event': event})
