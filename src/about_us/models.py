from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django_ckeditor_5.fields import CKEditor5Field


class AboutUs(models.Model):
    title = models.CharField(max_length=255, default="About Us")
    content = CKEditor5Field('Text', config_name='extends')
    image = models.ImageField(upload_to='about_us/', blank=True, null=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "About Us"


class CorporateProfile(models.Model):
    title = models.CharField(max_length=255, default="Corporate Profile")
    slug = models.SlugField(unique=True, blank=True)
    content = CKEditor5Field('Text', config_name='extends')
    image = models.ImageField(upload_to='corporate_profile/', blank=True, null=True)
    last_updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('about_corporate_profile', kwargs={'slug': self.slug})
    
    class Meta:
        verbose_name_plural = "Corporate Profiles"
