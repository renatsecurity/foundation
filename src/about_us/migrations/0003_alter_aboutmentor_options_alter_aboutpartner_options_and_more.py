# Generated by Django 5.1.6 on 2025-02-19 11:47

import django_ckeditor_5.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about_us', '0002_aboutus'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aboutmentor',
            options={'verbose_name_plural': 'About Mentors'},
        ),
        migrations.AlterModelOptions(
            name='aboutpartner',
            options={'verbose_name_plural': 'About Partners'},
        ),
        migrations.AlterModelOptions(
            name='aboutus',
            options={'verbose_name_plural': 'About Us'},
        ),
        migrations.AlterModelOptions(
            name='corporateprofile',
            options={'verbose_name_plural': 'Corporate Profiles'},
        ),
        migrations.AlterModelOptions(
            name='getinvolved',
            options={'verbose_name_plural': 'Get Involved'},
        ),
        migrations.AlterModelOptions(
            name='missionvision',
            options={'verbose_name_plural': 'Mission & Vision'},
        ),
        migrations.AlterModelOptions(
            name='upcomingevent',
            options={'verbose_name_plural': 'Upcoming Events'},
        ),
        migrations.AddField(
            model_name='aboutus',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='about_us/'),
        ),
        migrations.AddField(
            model_name='corporateprofile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='corporate_profile/'),
        ),
        migrations.AddField(
            model_name='getinvolved',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='get_involved/'),
        ),
        migrations.AddField(
            model_name='missionvision',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='mission_vision/'),
        ),
        migrations.AlterField(
            model_name='aboutmentor',
            name='bio',
            field=django_ckeditor_5.fields.CKEditor5Field(verbose_name='Text'),
        ),
        migrations.AlterField(
            model_name='aboutpartner',
            name='description',
            field=django_ckeditor_5.fields.CKEditor5Field(verbose_name='Text'),
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='content',
            field=django_ckeditor_5.fields.CKEditor5Field(verbose_name='Text'),
        ),
        migrations.AlterField(
            model_name='corporateprofile',
            name='content',
            field=django_ckeditor_5.fields.CKEditor5Field(verbose_name='Text'),
        ),
        migrations.AlterField(
            model_name='getinvolved',
            name='content',
            field=django_ckeditor_5.fields.CKEditor5Field(verbose_name='Text'),
        ),
        migrations.AlterField(
            model_name='missionvision',
            name='content',
            field=django_ckeditor_5.fields.CKEditor5Field(verbose_name='Text'),
        ),
        migrations.AlterField(
            model_name='upcomingevent',
            name='description',
            field=django_ckeditor_5.fields.CKEditor5Field(verbose_name='Text'),
        ),
    ]
