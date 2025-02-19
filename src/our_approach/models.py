from django.db import models
from django.utils.text import slugify
from django.urls import reverse


class OurApproach(models.Model):
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to='our_approach/', blank=True, null=True)
    youtube_video = models.URLField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('our_approach_detail', kwargs={'slug': self.slug})
