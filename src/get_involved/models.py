from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django_ckeditor_5.fields import CKEditor5Field


class OpportunityCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('get_involved_category_detail', args=[self.slug])
    
    class Meta:
        verbose_name_plural = "Opportunity Categories"
        ordering = ['name']


class Opportunity(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    description = CKEditor5Field('Description', config_name='extends')
    category = models.ForeignKey(OpportunityCategory, on_delete=models.CASCADE, related_name='opportunities')
    image = models.ImageField(upload_to='opportunity_images/', blank=True, null=True)
    deadline = models.DateField(null=True, blank=True)
    contact_email = models.EmailField()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('get_involved_detail', args=[self.slug])
    
    class Meta:
        verbose_name_plural = "Opportunities"
        ordering = ['title']
