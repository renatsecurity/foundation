from django.db import models
from django.urls import reverse
from django.utils.text import slugify

class Resource(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField()
    file = models.FileField(upload_to='resources/')
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('resources:resource_detail', args=[self.slug])
