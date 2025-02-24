from django.shortcuts import render, get_object_or_404
from .models import Testimonial


def testimonials_list(request):
    region = request.GET.get('region')
    sector = request.GET.get('sector')
    testimonials = Testimonial.objects.all()

    if region:
        testimonials = testimonials.filter(region=region)
    if sector:
        testimonials = testimonials.filter(sector=sector)

    regions = Testimonial.REGION_CHOICES
    sectors = Testimonial.SECTOR_CHOICES

    return render(request, "testimonials/testimonials_list.html", {
        "testimonials": testimonials,
        "regions": regions,
        "sectors": sectors,
        "selected_region": region,
        "selected_sector": sector,
    })


def testimonial_detail(request, slug):
    testimonial = get_object_or_404(Testimonial, slug=slug)
    return render(request, "testimonials/testimonial_detail.html", {"testimonial": testimonial})
