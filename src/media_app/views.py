from django.core.paginator import Paginator
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from taggit.models import Tag
from .models import News, PressRelease, Podcast, Category, Comment
from .forms import CommentForm, ReplyForm


def custom_error_404_view(request, exception):
    return render(request, "404.html", {})

def custom_error_500_view(request, exception=None):
    return render(request, "500.html", {})


def get_absolute_url(self):
    return reverse('news:news_list_by_tag', args=[self.slug])


# Add a method to the Tag model to get the absolute URL for news list page by tag
Tag.add_to_class('get_absolute_url', get_absolute_url)


def news_list(request, tag_slug=None):
    tag = None
    # Get all published news
    news = News.objects.filter(is_published=True)

    # Paginate news
    paginator = Paginator(news, 10)  # 10 items per page

    page_number = request.GET.get('page')  # Get current page number
    page_obj = paginator.get_page(page_number)  # Get page object

    # Get news by tag
    if tag_slug:
        tag = get_object_or_404(
            Tag,
            slug=tag_slug
        )
        news = news.filter(tags=tag)
    context = {
        'tag': tag,
        'page_obj': page_obj,
    }
    return render(request, 'media_app/blog.html', context)


def news_detail(request, slug):
    news_item = get_object_or_404(News, slug=slug)
    tags = Tag.objects.all()[:10]
    categories = Category.objects.all()[:10]
    recent_news = News.objects.filter(is_published=True).order_by('-published_date')[:5]
    # Get comments for the news
    comments = news_item.comments.filter(parent=None, is_approved=True)  # Only approved comments

    # Prepare comments with approved replies
    for comment in comments:
        comment.approved_replies = comment.replies.filter(is_approved=True)
    
    if request.method == "POST":
        if "comment_submit" in request.POST:  # Top-level comment submission
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                name = request.POST.get('name')
                email = request.POST.get('email')
                comment = comment_form.save(commit=False)
                comment.name = name
                comment.email = email
                comment.news = news_item
                comment.save()  # Saved as not approved
                return redirect('media_app:news_detail', slug=slug)

        elif "reply_submit" in request.POST:  # Reply submission
            reply_form = ReplyForm(request.POST)
            if reply_form.is_valid():
                name = request.POST.get('name')
                email = request.POST.get('email')
                reply = reply_form.save(commit=False)
                reply.name = name
                reply.email = email
                reply.news = news_item
                parent_id = request.POST.get("parent_id")
                if parent_id:
                    reply.parent = Comment.objects.get(id=parent_id)
                reply.save()  # Saved as not approved
                return redirect('media_app:news_detail', slug=slug)
    else:
        comment_form = CommentForm()
        reply_form = ReplyForm()
    
    context = {
        'categories': categories,
        'news_item': news_item,
        'recent_news': recent_news,
        'tags': tags,
        'comment_form': comment_form,
        'reply_form': reply_form,
    }
    return render(request, 'media_app/blog-details.html', context)


def press_release_list(request):
    press_releases = PressRelease.objects.all()
    return render(request, 'media_app/press_release_list.html', {'press_releases': press_releases})


def press_release_detail(request, slug):
    press_release = get_object_or_404(PressRelease, slug=slug)
    return render(request, 'media_app/press_release_detail.html', {'press_release': press_release})


def podcast_list(request):
    podcasts = Podcast.objects.all()
    return render(request, 'media_app/podcast_list.html', {'podcasts': podcasts})


def podcast_detail(request, slug):
    podcast = get_object_or_404(Podcast, slug=slug)
    return render(request, 'media_app/podcast_detail.html', {'podcast': podcast})
