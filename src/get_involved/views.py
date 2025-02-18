from django.shortcuts import render, get_object_or_404
from .models import Opportunity, OpportunityCategory


def get_involved_list(request):
    opportunities = Opportunity.objects.all().order_by('-deadline')
    categories = OpportunityCategory.objects.all()
    context = {'opportunities': opportunities, 'categories': categories}
    return render(request, 'get_involved/get_involved_list.html', context)


def get_involved_detail(request, slug):
    opportunity = get_object_or_404(Opportunity, slug=slug)
    return render(request, 'get_involved/get_involved_detail.html', {'opportunity': opportunity})


def get_involved_category_detail(request, slug):
    category = get_object_or_404(OpportunityCategory, slug=slug)
    opportunities = category.opportunities.all()
    context = {'category': category, 'opportunities': opportunities}
    return render(request, 'get_involved/get_involved_category_detail.html', context)
