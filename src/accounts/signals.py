from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.dispatch import receiver
from django.utils.timezone import now
from .models import UserActivity

@receiver(user_logged_in)
def log_login(sender, request, user, **kwargs):
    ip = get_client_ip(request)
    UserActivity.objects.create(user=user, action="Logged in", ip_address=ip)

@receiver(user_logged_out)
def log_logout(sender, request, user, **kwargs):
    ip = get_client_ip(request)
    UserActivity.objects.create(user=user, action="Logged out", ip_address=ip)

@receiver(user_login_failed)
def log_failed_login(sender, credentials, request, **kwargs):
    ip = get_client_ip(request)
    UserActivity.objects.create(user=None, action="Failed login attempt", ip_address=ip)

def get_client_ip(request):
    """Get client IP address from request headers."""
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        ip = x_forwarded_for.split(",")[0]
    else:
        ip = request.META.get("REMOTE_ADDR")
    return ip
