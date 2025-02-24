from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Impact, Country, Category


def impact_list(request):
    impacts = Impact.objects.all().order_by('-date')
    countries = Country.objects.all()
    categories = Category.objects.all()
    context = {
        'impacts': impacts,
        'countries': countries,
        'categories': categories,
    }
    return render(request, 'impact/impact_list.html', context)


def impact_detail(request, slug):
    impact = get_object_or_404(Impact, slug=slug)
    return render(request, 'impact/impact_detail.html', {'impact': impact})


def country_chart_data(request):
    countries = Country.objects.all()
    data = {
        "labels": [country.name for country in countries],
        "values": [country.impact_value for country in countries],
    }
    return JsonResponse(data)


def category_chart_data(request):
    categories = Category.objects.all()
    data = {
        "labels": [category.name for category in categories],
        "values": [category.impact_value for category in categories],
    }
    return JsonResponse(data)
