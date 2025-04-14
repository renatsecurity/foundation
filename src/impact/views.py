from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Impact, State, Category


def impact_list(request):
    impacts = Impact.objects.all().order_by('-date')
    states = State.objects.all()
    categories = Category.objects.all()
    context = {
        'impacts': impacts,
        'states': states,
        'categories': categories,
    }
    return render(request, 'impact/impact_list.html', context)


def impact_detail(request, slug):
    impact = get_object_or_404(Impact, slug=slug)
    return render(request, 'impact/impact_detail.html', {'impact': impact})


def state_chart_data(request):
    states = State.objects.all()
    data = {
        "labels": [state.name for state in states],
        "values": [state.impact_value for state in states],
    }
    return JsonResponse(data)


def category_chart_data(request):
    categories = Category.objects.all()
    data = {
        "labels": [category.name for category in categories],
        "values": [category.impact_value for category in categories],
    }
    return JsonResponse(data)
