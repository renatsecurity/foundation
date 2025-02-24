from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Testimonial(models.Model):
    REGION_CHOICES = [
        ('East Africa', 'East Africa'),
        ('North Africa', 'North Africa'),
        ('South Africa', 'South Africa'),
        ('West Africa', 'West Africa'),
        ('Central Africa', 'Central Africa'),
    ]

    SECTOR_CHOICES = [
        ('Agriculture', 'Agriculture'),
        ('Technology', 'Technology'),
        ('Health', 'Health'),
        ('Education', 'Education'),
        ('Finance', 'Finance'),
        ('Fashion', 'Fashion'),
    ]

    name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='testimonials/', blank=True, null=True)
    message = models.TextField()
    rating = models.PositiveSmallIntegerField(default=5, choices=[(i, i) for i in range(1, 6)])
    slug = models.SlugField(unique=True, blank=True)
    region = models.CharField(max_length=50, choices=REGION_CHOICES, blank=True, null=True)
    sector = models.CharField(max_length=50, choices=SECTOR_CHOICES, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} - {self.designation}"
    
    class Meta:
        verbose_name_plural = "Testimonials"
    
    def get_absolute_url(self):
        return reverse("testimonial_detail", kwargs={"slug": self.slug})
