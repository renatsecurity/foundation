from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Mentor(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    bio = models.TextField()
    expertise = models.CharField(max_length=255)
    image = models.ImageField(upload_to='mentor_images/', blank=True, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('mentor_detail', args=[self.slug])
