# Generated by Django 5.1.6 on 2025-02-18 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('description', models.TextField()),
                ('file', models.FileField(upload_to='resources/')),
                ('published_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
