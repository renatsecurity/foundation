from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django_ckeditor_5.fields import CKEditor5Field


class BaseMedia(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    content = CKEditor5Field('Text', config_name='extends')
    published_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
        ordering = ['-published_date']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class News(BaseMedia):
    def get_absolute_url(self):
        return reverse('media_app:news_detail', args=[self.slug])


class PressRelease(BaseMedia):
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
