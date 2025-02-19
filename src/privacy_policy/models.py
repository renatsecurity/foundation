from django.db import models
from django.urls import reverse
from django_ckeditor_5.fields import CKEditor5Field


class PrivacyPolicy(models.Model):
    title = models.CharField(max_length=255, default="Privacy Policy")
    content = CKEditor5Field('Text', config_name='extends')
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('privacy_policy')
    
    class Meta:
        verbose_name_plural = "Privacy Policy"
