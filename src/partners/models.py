from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django_ckeditor_5.fields import CKEditor5Field

class PartnerGroup(models.Model):
    title = models.CharField(max_length=255)
    description = CKEditor5Field('Text', config_name='extends')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "Partner Groups"


class Partner(models.Model):
    group = models.ForeignKey(PartnerGroup, on_delete=models.CASCADE, related_name='partners')
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    description = CKEditor5Field('Text', config_name='extends')
    website = models.URLField(blank=True, null=True)
    logo = models.ImageField(upload_to='partner_logos/', blank=True, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('partner_detail', args=[self.slug])
    
    class Meta:
        verbose_name_plural = "Partners"
