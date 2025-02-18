from django.db import models
from django.urls import reverse
from django.utils.text import slugify

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


class Article(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    category = models.ForeignKey(TopicCategory, on_delete=models.CASCADE, related_name='articles')
    content = models.TextField()
    image = models.ImageField(upload_to='gender_and_green_images/')
    author = models.CharField(max_length=100)
    published_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('gender_and_green_detail', args=[self.slug])
