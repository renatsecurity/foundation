from django.db import models
from django_ckeditor_5.fields import CKEditor5Field


class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = CKEditor5Field('Answer', config_name='extends')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question
    
    class Meta:
        verbose_name_plural = "FAQs"
        ordering = ['-created_at']
