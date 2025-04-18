from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django_ckeditor_5.fields import CKEditor5Field


class Career(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    description = CKEditor5Field('Description', config_name='extends')
    requirements = CKEditor5Field('Requirements', config_name='extends')
    location = models.CharField(max_length=255)
    image = models.ImageField(upload_to="michaelanoka/career/", blank=True, null=True)
    posted_date = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField()
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('career_detail', args=[self.slug])
    
    class Meta:
        verbose_name_plural = "Careers"
        ordering = ['-posted_date']
