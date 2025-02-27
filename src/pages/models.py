from django.db import models
from django_ckeditor_5.fields import CKEditor5Field


class Slider(models.Model):
    title = models.CharField(max_length=100)
    description = CKEditor5Field('Text', config_name='extends')
    image = models.ImageField(upload_to='slider/', blank=True, null=True)
    link = models.URLField(max_length=200, blank=True, null=True)
    is_visible = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Slider'
        verbose_name_plural = 'Sliders'

    def __str__(self):
        return self.title


class DidYouKnow(models.Model):
    description = CKEditor5Field('Text', config_name='extends')
    is_visible = models.BooleanField(default=True)
    background_image = models.ImageField(upload_to='did_you_knows/', blank=True, null=True)
    background_color = models.CharField(max_length=100, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Did You Know'
        verbose_name_plural = 'Did You Knows'

    def __str__(self):
        return self.description[:25]
