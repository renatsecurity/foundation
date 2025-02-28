from django.http import HttpResponse


def robots_txt(request):
    lines = [
        "User-agent: *",
        "Disallow: /admin/",  # Prevent crawlers from accessing the admin area
        "Disallow: /twofactor/",
        "Disallow: /accounts/",
        "Disallow: /secrets/",
        "Disallow: /as/",
        "Disallow: /accounts/profile/",
        "Disallow: /accounts/password_change/",
        "Disallow: /accounts/password_change/done/",
        "Disallow: /accounts/logout/",
        "Disallow: /accounts/login/",
        "Disallow: /accounts/register/",
        "Disallow: /accounts/activate/",
        "Disallow: /accounts/resend_activation/",
        "Disallow: /accounts/reset_password/",
        "Disallow: /accounts/reset_password_confirm/",
        "Disallow: /accounts/reset_password_complete/",
        "Disallow: /accounts/confirm/",
        "Disallow: /accounts/confirm_complete/",
        "Disallow: /accounts/password_reset/",
        "Disallow: /accounts/password_reset/done/",
        "Disallow: /login/",
        "Disallow: /signup/",
        "Disallow: /logout/",
        "Disallow: /password_reset/",
        "Disallow: /password_reset/done/",
        "Disallow: /password_reset/confirm/",
        "Disallow: /password_reset/complete/",
        "Allow: /",
        "Allow: /about-us/",
        "Allow: /faqs/",
        "Allow: /media_urls/",
        "Allow: /events/",
        "Allow: /impact/",
        "Allow: /mentors/",
        "Allow: /partners/",
        "Allow: /events/",
        "Allow: /careers/",
        "Allow: /gender-and-green/",
        "Allow: /get-involved/",
        "Allow: /safeguard-policy/",
        "Allow: /privacy-policy/",
        "Allow: /resources/",
        "Allow: /research/",
        "Allow: /terms-and-conditions/",
        "Allow: /testimonials/"
        "Allow: /sitemap.xml",
        
        # "Sitemap: https://renatwebsite.com/sitemap.xml",
        "Sitemap: http://127.0.0.1:8000/sitemap.xml",
    ]

    return HttpResponse("\n".join(lines), content_type="text/plain")
