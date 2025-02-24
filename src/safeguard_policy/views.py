from django.shortcuts import render, get_object_or_404
from .models import SafeguardPolicy


def policy_list(request):
    policy = SafeguardPolicy.objects.order_by('-last_updated').first()
    return render(request, 'safeguard_policy/policy_list.html', {'policy': policy})


def policy_detail(request, id):
    policy = get_object_or_404(SafeguardPolicy, id=id)
    return render(request, 'safeguard_policy/policy_detail.html', {'policy': policy})
