import json
from django.shortcuts import render
from .models import PastProgramme


def past_programmes(request):
    programmes = PastProgramme.objects.all()
    programmes_dict = {p.title: p.content for p in programmes}
    context = {
        'programmes': programmes,
        'programmes_json': json.dumps(programmes_dict)
    }
    return render(request, 'past_programmes/programmes.html', context)

