# Generated by Django 5.1.6 on 2025-02-19 11:47

import django_ckeditor_5.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gender_and_green', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-published_date'], 'verbose_name_plural': 'Articles'},
        ),
        migrations.AlterModelOptions(
            name='topiccategory',
            options={'ordering': ['name'], 'verbose_name_plural': 'Topic Categories'},
        ),
        migrations.AlterField(
            model_name='article',
            name='content',
            field=django_ckeditor_5.fields.CKEditor5Field(verbose_name='Text'),
        ),
    ]
