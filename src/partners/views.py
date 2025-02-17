from django.shortcuts import render, get_object_or_404
from .models import PartnerGroup, Partner

def partner_list(request):
    groups = PartnerGroup.objects.prefetch_related('partners').all()
    return render(request, 'partners/partner_list.html', {'groups': groups})

def partner_detail(request, slug):
    partner = get_object_or_404(Partner, slug=slug)
    return render(request, 'partners/partner_detail.html', {'partner': partner})
