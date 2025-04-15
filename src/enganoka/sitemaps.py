from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from media_app.models import News, PressRelease, Podcast
from careers.models import Career
from events.models import Event
from get_involved.models import Opportunity
from gender_and_green.models import Article
from impact.models import Impact
from past_programmes.models import PastProgramme
from research.models import Research
from resources.models import Resource


class NewsModelSitemap(Sitemap):
    changefreq = "daily"  # Frequency of updates ('always', 'hourly', 'daily', etc.)
    priority = 0.8        # Priority of this page relative to others (0.0 to 1.0)

    def items(self):
        return News.objects.filter(is_published=True).all()

    def lastmod(self, obj):
        return obj.updated_date

    def location(self, obj):
        return reverse('media_app:news_detail', args=[obj.slug])


class PressReleaseModelSitemap(Sitemap):
    changefreq = "weekly"  # Frequency of updates ('always', 'hourly', 'daily', etc.)
    priority = 0.8        # Priority of this page relative to others (0.0 to 1.0)

    def items(self):
        return PressRelease.objects.filter(is_published=True).all()

    def lastmod(self, obj):
        return obj.updated_date

    def location(self, obj):
        return reverse('media_app:press_release_detail', args=[obj.slug])


class PodcastModelSitemap(Sitemap):
    changefreq = "weekly"  # Frequency of updates ('always', 'hourly', 'daily', etc.)
    priority = 0.8        # Priority of this page relative to others (0.0 to 1.0)

    def items(self):
        return Podcast.objects.all()

    def lastmod(self, obj):  # Last modified date
        return obj.updated_date

    def location(self, obj):
        return reverse('media_app:podcast_detail', args=[obj.slug])


class CareerModelSitemap(Sitemap):
    changefreq = "weekly"  # Frequency of updates ('always', 'hourly', 'daily', etc.)
    priority = 0.8        # Priority of this page relative to others (0.0 to 1.0)

    def items(self):
        return Career.objects.all()

    def lastmod(self, obj):  # Last modified date
        return obj.last_updated

    def location(self, obj):
        return reverse('career_detail', args=[obj.slug])


class EventModelSitemap(Sitemap):
    changefreq = "weekly"  # Frequency of updates ('always', 'hourly', 'daily', etc.)
    priority = 0.8        # Priority of this page relative to others (0.0 to 1.0)

    def items(self):
        return Event.objects.all()

    def lastmod(self, obj):  # Last modified date
        return obj.last_updated

    def location(self, obj):
        return reverse('event_detail', args=[obj.slug])


class OpportunityModelSitemap(Sitemap):
    changefreq = "weekly"  # Frequency of updates ('always', 'hourly', 'daily', etc.)
    priority = 0.8        # Priority of this page relative to others (0.0 to 1.0)

    def items(self):
        return Opportunity.objects.all()

    def lastmod(self, obj):  # Last modified date
        return obj.last_updated

    def location(self, obj):
        return reverse('get_involved_detail', args=[obj.slug])


class ArticleModelSitemap(Sitemap):
    changefreq = "weekly"  # Frequency of updates ('always', 'hourly', 'daily', etc.)
    priority = 0.8        # Priority of this page relative to others (0.0 to 1.0)

    def items(self):
        return Article.objects.filter(is_published=True).all()

    def lastmod(self, obj):  # Last modified date
        return obj.updated_date

    def location(self, obj):
        return reverse('gender_and_green_detail', args=[obj.slug])


class ImpactModelSitemap(Sitemap):
    changefreq = "weekly"  # Frequency of updates ('always', 'hourly', 'daily', etc.)
    priority = 0.8        # Priority of this page relative to others (0.0 to 1.0)

    def items(self):
        return Impact.objects.filter(is_published=True).all()

    def lastmod(self, obj):  # Last modified date
        return obj.last_updated

    def location(self, obj):
        return reverse('impact:impact_detail', args=[obj.slug])


class PastProgrammeModelSitemap(Sitemap):
    changefreq = "weekly"  # Frequency of updates ('always', 'hourly', 'daily', etc.)
    priority = 0.8        # Priority of this page relative to others (0.0 to 1.0)

    def items(self):
        return PastProgramme.objects.filter(is_published=True).all()

    def lastmod(self, obj):  # Last modified date
        return obj.last_updated

    def location(self, item):
        return reverse(item)


class ResearchModelSitemap(Sitemap):
    changefreq = "weekly"  # Frequency of updates ('always', 'hourly', 'daily', etc.)
    priority = 0.8        # Priority of this page relative to others (0.0 to 1.0)

    def items(self):
        return Research.objects.filter(is_published=True).all()

    def lastmod(self, obj):  # Last modified date
        return obj.last_updated

    def location(self, obj):
        return reverse('research_detail', args=[obj.slug])


class ResourceModelSitemap(Sitemap):
    changefreq = "weekly"  # Frequency of updates ('always', 'hourly', 'daily', etc.)
    priority = 0.8        # Priority of this page relative to others (0.0 to 1.0)

    def items(self):
        return Resource.objects.filter(is_published=True).all()

    def lastmod(self, obj):  # Last modified date
        return obj.last_updated

    def location(self, obj):
        return reverse('resources:resource_detail', args=[obj.slug])


class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'monthly'

    def items(self):
        return [
            'pages:index', 'about_us',
            'faq_list', 'our_approach_list',
            'privacy_policy', 'safeguard_policy_list',
            'terms_and_conditions', 'testimonials_list'
        ]  # URL names of static pages

    def location(self, item):
        return reverse(item)
