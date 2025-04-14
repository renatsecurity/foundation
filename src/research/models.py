from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django_ckeditor_5.fields import CKEditor5Field


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
    
    class Meta:
        verbose_name_plural = "Research Categories"


class Research(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    abstract = CKEditor5Field('Content', config_name='extends')
    image = models.ImageField(upload_to='research_images/', blank=True, null=True)
    author = models.CharField(max_length=255)
    publication_date = models.DateField()
    document = models.FileField(upload_to='research_papers/', blank=True, null=True)
    category = models.ForeignKey(ResearchCategory, on_delete=models.CASCADE, related_name='research_papers')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('research_detail', args=[self.slug])
    
    class Meta:
        verbose_name_plural = "Research Papers"
