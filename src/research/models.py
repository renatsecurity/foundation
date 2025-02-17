from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class ResearchCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('research_category_detail', args=[self.slug])


class Research(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    abstract = models.TextField()
    author = models.CharField(max_length=255)
    publication_date = models.DateField()
    document = models.FileField(upload_to='research_papers/')
    category = models.ForeignKey(ResearchCategory, on_delete=models.CASCADE, related_name='research_papers')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('research_detail', args=[self.slug])
