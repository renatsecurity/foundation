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


class MissionVision(models.Model):
    title = models.CharField(max_length=255, default="Our Mission & Vision")
    slug = models.SlugField(unique=True, blank=True)
    content = CKEditor5Field('Text', config_name='extends')
    image = models.ImageField(upload_to='mission_vision/', blank=True, null=True)
    last_updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('about_mission_vision', kwargs={'slug': self.slug})
    
    class Meta:
        verbose_name_plural = "Mission & Vision"


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


class AboutPartner(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    description = CKEditor5Field('Text', config_name='extends')
    website = models.URLField(blank=True, null=True)
    logo = models.ImageField(upload_to='partners/', blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('about_partner_detail', kwargs={'slug': self.slug})
    
    class Meta:
        verbose_name_plural = "About Partners"


class AboutMentor(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    bio = CKEditor5Field('Text', config_name='extends')
    photo = models.ImageField(upload_to='mentors/', blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('about_mentor_detail', kwargs={'slug': self.slug})
    
    class Meta:
        verbose_name_plural = "About Mentors"


class GetInvolved(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    content = CKEditor5Field('Text', config_name='extends')
    image = models.ImageField(upload_to='get_involved/', blank=True, null=True)
    last_updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('about_get_involved', kwargs={'slug': self.slug})
    
    class Meta:
        verbose_name_plural = "Get Involved"


class UpcomingEvent(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    description = CKEditor5Field('Text', config_name='extends')
    date = models.DateTimeField()
    location = models.CharField(max_length=255)
    image = models.ImageField(upload_to='events/', blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('about_upcoming_event_detail', kwargs={'slug': self.slug})
    
    class Meta:
        verbose_name_plural = "Upcoming Events"
