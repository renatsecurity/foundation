from django.shortcuts import render, get_object_or_404
from .models import Mentor


def mentor_list(request):
    mentors = Mentor.objects.all().order_by('name')
    return render(request, 'mentor/mentor_list.html', {'mentors': mentors})

def mentor_detail(request, slug):
    mentor = get_object_or_404(Mentor, slug=slug)
    return render(request, 'mentor/mentor_detail.html', {'mentor': mentor})