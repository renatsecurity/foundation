from django.db import models
from django.urls import reverse
from django.utils.text import slugify

class MediaType(models.TextChoices):
    NEWS = 'News', 'News'
    ARTICLE = 'Article', 'Article'
    BLOG = 'Blog', 'Blog'
    PRESS_RELEASE = 'Press Release', 'Press Release'

class Media(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    content = models.TextField()
    media_type = models.CharField(max_length=20, choices=MediaType.choices)
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('media_app:media_detail', args=[self.slug])

    def get_media_type_url(self):
        return reverse('media_app:media_type_list', args=[self.media_type.lower().replace(' ', '-')])
