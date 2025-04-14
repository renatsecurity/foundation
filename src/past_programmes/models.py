from django.db import models
from django_ckeditor_5.fields import CKEditor5Field


class PastProgramme(models.Model):
    title = models.CharField(max_length=100, help_text="Title of the past programme. E.g. 'MAF CHARITY OUTREACH'")
    content = CKEditor5Field('Content', config_name='extends', help_text="Summary of the past programme and what it covered in well-detailed.")
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
