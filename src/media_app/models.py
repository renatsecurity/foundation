from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django_ckeditor_5.fields import CKEditor5Field
from taggit.managers import TaggableManager


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('media_app:news_category', args=[self.slug])


class BaseMedia(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    content = CKEditor5Field('Text', config_name='extends')
    published_date = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)

    class Meta:
        abstract = True
        ordering = ['-published_date']
        get_latest_by = '-published_date'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class News(BaseMedia):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='news_images/', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="news")
    tags = TaggableManager()

    def get_absolute_url(self):
        return reverse('media_app:news_detail', args=[self.slug])
    
    def get_comments(self):
        return Comment.objects.filter(news=self).order_by('-created_at')


class Comment(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=100)
    email = models.EmailField()
    content = models.TextField()
    parent = models.ForeignKey(
        'self', null=True, blank=True, on_delete=models.CASCADE, related_name="replies"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('media_app:news_detail', args=[self.news.slug]) + f"#comment-{self.id}"

    def __str__(self):
        return f"Comment by {self.name} on {self.news.title}"
    
    class Meta:
        ordering = ['-created_at']


class PressRelease(BaseMedia):
    file = models.FileField(upload_to='press_releases/', blank=True, null=True)
    def get_absolute_url(self):
        return reverse('media_app:press_release_detail', args=[self.slug])


class Podcast(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    cloudflare_link = models.URLField(help_text="Direct Cloudflare link to the audio file")
    published_date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('media_app:podcast_detail', args=[self.slug])
