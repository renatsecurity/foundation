# Generated by Django 5.1.6 on 2025-02-19 11:47

import django_ckeditor_5.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('media_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='media',
            options={'ordering': ['-published_date'], 'verbose_name_plural': 'Media'},
        ),
        migrations.AlterField(
            model_name='media',
            name='content',
            field=django_ckeditor_5.fields.CKEditor5Field(verbose_name='Text'),
        ),
    ]
