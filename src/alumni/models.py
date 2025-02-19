from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django_ckeditor_5.fields import CKEditor5Field

class Alumni(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    graduation_year = models.IntegerField()
    occupation = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    bio = CKEditor5Field('Text', config_name='extends')
    linkedin_url = models.URLField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='alumni_pictures/', blank=True, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('alumni:alumni_detail', args=[self.slug])
    
    class Meta:
        verbose_name_plural = "Alumni"
