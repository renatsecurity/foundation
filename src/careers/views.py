from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Career


def career_list(request):
    careers = Career.objects.all().order_by('-posted_date')
    # Paginate news
    paginator = Paginator(careers, 10)  # 10 items per page

    page_number = request.GET.get('page')  # Get current page number
    page_obj = paginator.get_page(page_number)  # Get page object

    return render(request, 'careers/career_list.html', {'page_obj': page_obj})


def career_detail(request, slug):
    career = get_object_or_404(Career, slug=slug)
    return render(request, 'careers/career_detail.html', {'career': career})
