from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.utils.timezone import now, timedelta
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.urls import reverse_lazy
from django.db.models import Count
from django.http import JsonResponse
from .models import CustomUser, Notification
from .forms import CustomAuthenticationForm, CustomUserCreationForm, ProfileUpdateForm
from .decorators import role_required
from .utils import send_notification_email

User = get_user_model()


def admin_analytics(request):
    total_users = User.objects.count()
    active_users = User.objects.filter(last_login__gte=now() - timedelta(days=30)).count()
    user_growth = (
        User.objects.extra(select={"day": "date(date_joined)"})
        .values("day")
        .annotate(count=Count("id"))
        .order_by("day")
    )

    return render(
        request,
        "accounts/admin_analytics.html",
        {
            "total_users": total_users,
            "active_users": active_users,
            "user_growth": user_growth,
        },
    )


def get_notifications(request):
    notifications = Notification.objects.filter(user=request.user, is_read=False)
    data = [{"message": n.message, "created_at": n.created_at} for n in notifications]
    return JsonResponse({"notifications": data})


class CustomPasswordResetView(PasswordResetView):
    template_name = "accounts/password_reset.html"
    email_template_name = "accounts/password_reset_email.html"
    success_url = reverse_lazy("password_reset_done")


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = "accounts/password_reset_confirm.html"
    success_url = reverse_lazy("login")


def send_verification_email(request, user):
    """Send email confirmation link to the user"""
    current_site = get_current_site(request)
    mail_subject = "Activate your account"
    message = render_to_string("accounts/email_verification.html", {
        "user": user,
        "domain": current_site.domain,
        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
        "token": default_token_generator.make_token(user),
    })
    email = EmailMessage(mail_subject, message, to=[user.email])
    email.send()

def activate_account(request, uidb64, token):
    """Activate the user account"""
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = CustomUser.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
        user = None

    if user and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        # Send Welcome Email
        subject = "Welcome to Engineer Michael Anoka Foundation"
        message = f"Hi {user.username}, welcome to our platform!"
        send_notification_email(subject, message, [user.email])
        return redirect("login")
    return render(request, "accounts/activation_failed.html")


@login_required
@role_required(["admin", "manager"])
def admin_dashboard(request):
    return render(request, "accounts/admin_dashboard.html")


@login_required
@role_required(["manager"])
def manager_dashboard(request):
    return render(request, "accounts/manager_dashboard.html")


def register_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user = form.save()
            send_verification_email(request, user)
            return render(request, "accounts/email_sent.html")
    else:
        form = CustomUserCreationForm()
    return render(request, "accounts/register.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("dashboard")
    else:
        form = CustomAuthenticationForm()
    return render(request, "accounts/login.html", {"form": form})


@login_required
def profile_view(request):
    if request.method == "POST":
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("profile")
    else:
        form = ProfileUpdateForm(instance=request.user)
    return render(request, "accounts/profile.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("login")
