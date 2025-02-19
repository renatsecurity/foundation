from django.shortcuts import render, get_object_or_404
from .models import MissionVision, CorporateProfile, AboutPartner, AboutMentor, GetInvolved, UpcomingEvent


# def mission_vision(request):
#     mission = MissionVision.objects.first()
#     return render(request, 'about_us/mission_vision.html', {'mission': mission})


def mission_vision(request, slug):
    mission = get_object_or_404(MissionVision, slug=slug)
    return render(request, 'about_us/mission_vision.html', {'mission': mission})


# def corporate_profile(request):
#     profile = CorporateProfile.objects.first()
#     return render(request, 'about_us/corporate_profile.html', {'profile': profile})


def corporate_profile(request, slug):
    profile = get_object_or_404(CorporateProfile, slug=slug)
    return render(request, 'about_us/corporate_profile.html', {'profile': profile})


def partners_list(request):
    partners = AboutPartner.objects.all()
    return render(request, 'about_us/partners_list.html', {'partners': partners})


def partner_detail(request, slug):
    partner = get_object_or_404(AboutPartner, slug=slug)
    return render(request, 'about_us/partner_detail.html', {'partner': partner})


def mentor_list(request):
    mentors = AboutMentor.objects.all()
    return render(request, 'about_us/mentor_list.html', {'mentors': mentors})


def mentor_detail(request, slug):
    mentor = get_object_or_404(AboutMentor, slug=slug)
    return render(request, 'about_us/mentor_detail.html', {'mentor': mentor})


def get_involved(request):
    opportunities = GetInvolved.objects.all()
    return render(request, 'about_us/get_involved.html', {'opportunities': opportunities})


def get_involved_detail(request, slug):
    opportunity = get_object_or_404(GetInvolved, slug=slug)
    return render(request, 'about_us/get_involved.html', {'opportunity': opportunity})


def upcoming_events(request):
    events = UpcomingEvent.objects.all().order_by('date')
    return render(request, 'about_us/upcoming_events.html', {'events': events})


def upcoming_event_detail(request, slug):
    event = get_object_or_404(UpcomingEvent, slug=slug)
    return render(request, 'about_us/upcoming_event_detail.html', {'event': event})
