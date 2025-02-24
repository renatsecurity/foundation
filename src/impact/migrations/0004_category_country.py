# Generated by Django 5.1.6 on 2025-02-24 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('impact', '0003_alter_impact_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('impact_value', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('impact_value', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
