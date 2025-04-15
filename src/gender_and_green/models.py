from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django_ckeditor_5.fields import CKEditor5Field

class TopicCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('gender_and_green_category_detail', args=[self.slug])
    
    class Meta:
        verbose_name_plural = "Topic Categories"
        ordering = ['name']


class Article(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    category = models.ForeignKey(TopicCategory, on_delete=models.CASCADE, related_name='articles')
    content = CKEditor5Field('Content', config_name='extends')
    image = models.ImageField(upload_to='gender_and_green_images/')
    author = models.CharField(max_length=100)
    published_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('gender_and_green_detail', args=[self.slug])
    
    class Meta:
        verbose_name_plural = "Articles"
        ordering = ['-published_date']
