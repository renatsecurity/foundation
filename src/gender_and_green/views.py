from django.shortcuts import render, get_object_or_404
from .models import Article, TopicCategory


def article_list(request):
    articles = Article.objects.all().order_by('-published_date')
    categories = TopicCategory.objects.all()
    return render(request, 'gender_and_green/article_list.html', {'articles': articles, 'categories': categories})


def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug)
    return render(request, 'gender_and_green/article_detail.html', {'article': article})


def category_detail(request, slug):
    category = get_object_or_404(TopicCategory, slug=slug)
    articles = category.articles.all()
    return render(request, 'gender_and_green/category_detail.html', {'category': category, 'articles': articles})
