from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django_ckeditor_5.fields import CKEditor5Field


class AboutUs(models.Model):
    title = models.CharField(max_length=255, default="About Us")
    content = CKEditor5Field('Text', config_name='extends')
    image = models.ImageField(upload_to='about_us/', blank=True, null=True)
    last_updated = models.DateTimeField(auto_now=True)
    youtube_video = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "About Us"


class MissionAndVision(models.Model):
    title = models.CharField(max_length=255, unique=True)
    description = CKEditor5Field('Text', config_name='extends')
    image = models.ImageField(upload_to='mission_vision/', blank=True, null=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Mission and Vision"


class CorporateProfile(models.Model):
    title = models.CharField(max_length=255, default="Corporate Profile")
    content = CKEditor5Field('Text', config_name='extends')
    image = models.ImageField(upload_to='corporate_profile/', blank=True, null=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "Corporate Profiles"
