from django.shortcuts import render
from .models import TermsAndConditions


def terms_and_conditions(request):
    terms = TermsAndConditions.objects.first()
    return render(request, 'terms_and_conditions/terms.html', {'terms': terms})
