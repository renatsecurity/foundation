from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class MissionVision(models.Model):
    title = models.CharField(max_length=255, default="Our Mission & Vision")
    slug = models.SlugField(unique=True, blank=True)
    content = models.TextField()
    last_updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('about_mission_vision', kwargs={'slug': self.slug})


class CorporateProfile(models.Model):
    title = models.CharField(max_length=255, default="Corporate Profile")
    slug = models.SlugField(unique=True, blank=True)
    content = models.TextField()
    last_updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('about_corporate_profile', kwargs={'slug': self.slug})


class AboutPartner(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField()
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


class AboutMentor(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    bio = models.TextField()
    photo = models.ImageField(upload_to='mentors/', blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('about_mentor_detail', kwargs={'slug': self.slug})


class GetInvolved(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    content = models.TextField()
    last_updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('about_get_involved', kwargs={'slug': self.slug})


class UpcomingEvent(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField()
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
