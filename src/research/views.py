from django.shortcuts import render, get_object_or_404
from .models import Research, ResearchCategory


def research_list(request):
    research_papers = Research.objects.all().order_by('-publication_date')
    categories = ResearchCategory.objects.all()
    context = {'research_papers': research_papers, 'categories': categories}
    return render(request, 'research/research_list.html', context)


def research_detail(request, slug):
    research = get_object_or_404(Research, slug=slug)
    return render(request, 'research/research_detail.html', {'research': research})


def research_category_detail(request, slug):
    category = get_object_or_404(ResearchCategory, slug=slug)
    research_papers = category.research_papers.all()
    context = {'category': category, 'research_papers': research_papers}
    return render(request, 'research/research_category_detail.html', context)
