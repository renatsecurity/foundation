import os
from django.shortcuts import render
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from django.conf import settings
from mentor.models import Mentor
from our_approach.models import OurApproach
from partners.models import Partner
from .models import AboutUs, CorporateProfile, MissionAndVision


def about_us(request):
    about = AboutUs.objects.first()
    mission_vision = MissionAndVision.objects.first()
    mentors = Mentor.objects.all()[:4]
    our_approaches = OurApproach.objects.all()[:4]
    partners = Partner.objects.all()
    context = {
        'about': about,
        'mission_vision': mission_vision,
        'mentors': mentors,
        'our_approaches': our_approaches,
        'partners': partners
    }
    return render(request, 'about_us/about.html', context)


def export_corporate_profile_to_pdf(request):
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = 'attachment; filename="CorporateProfile.pdf"'

    pdf = canvas.Canvas(response)
    pdf.setTitle("Corporate Profiles")

    news_items = CorporateProfile.objects.all()
    y_position = 800  # Start position for text

    pdf.setFont("Helvetica-Bold", 14)
    pdf.drawString(200, y_position, "Corporate Profiles")
    pdf.line(200, y_position - 5, 400, y_position - 5)
    y_position -= 40

    pdf.setFont("Helvetica", 12)
    for news in news_items:
        pdf.drawString(100, y_position, f"Title: {news.title}")
        y_position -= 20
        pdf.drawString(100, y_position, f"Published Date: {news.last_updated.strftime('%Y-%m-%d')}")
        y_position -= 20

        # Display image if available
        if news.image:
            image_path = os.path.join(settings.MEDIA_ROOT, news.image.name)
            if os.path.exists(image_path):  # Check if image exists
                pdf.drawImage(ImageReader(image_path), 100, y_position - 100, width=200, height=100)
                y_position -= 120  # Space below image

        # Truncate long content and wrap text
        content_text = news.content[:200] + "..." if len(news.content) > 200 else news.content
        pdf.drawString(100, y_position, f"Content: {content_text}")
        y_position -= 40

        if y_position < 100:  # Page break
            pdf.showPage()
            y_position = 800

    pdf.save()
    return response


def corporate_profile(request):
    profiles = CorporateProfile.objects.all()
    return render(request, 'about_us/corporate_profile.html', {'profiles': profiles})
