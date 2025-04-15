from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django_ckeditor_5.fields import CKEditor5Field


class Impact(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    description = CKEditor5Field('Description', config_name='extends')
    date = models.DateField()
    image = models.ImageField(upload_to='impact_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    state = models.ForeignKey('State', on_delete=models.SET_NULL, null=True, blank=True)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('impact:impact_detail', args=[self.slug])

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "Impact"
        ordering = ['-date']


class State(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(unique=True, blank=True)
    impact_value = models.PositiveIntegerField(default=0)  # Example metric

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(unique=True, blank=True)
    impact_value = models.PositiveIntegerField(default=0)  # Example metric

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
