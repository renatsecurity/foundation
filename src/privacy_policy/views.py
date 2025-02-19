from django.shortcuts import render
from .models import PrivacyPolicy

def privacy_policy(request):
    policy = PrivacyPolicy.objects.first()
    return render(request, 'privacy_policy/privacy_policy.html', {'policy': policy})
