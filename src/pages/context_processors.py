from newsletter.models import Newsletter


def latest_newsletter(request):
    # Try to get the most recent newsletter title
    latest_newsletter = Newsletter.objects.first()
    
    # Return the context with the title or a default message
    return {
        'latest_newsletter_title': latest_newsletter.slug if latest_newsletter else "No newsletters available"
    }
