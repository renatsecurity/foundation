from django.contrib.auth import views as auth_views
from django.urls import path
from .views import (
    register_view, login_view, logout_view,
    activate_account, profile_view,
    admin_dashboard, manager_dashboard,
)


urlpatterns = [
    path("register/", register_view, name="register"),
    path("activate/<uidb64>/<token>/", activate_account, name="activate"),
    path("login/", login_view, name="login"),
    path("profile/", profile_view, name="profile"),
    path("admin_dashboard/", admin_dashboard, name="admin_dashboard"),
    path("manager_dashboard/", manager_dashboard, name="manager_dashboard"),
    path("logout/", logout_view, name="logout"),
    path("password_reset/", auth_views.PasswordResetView.as_view(), name="password_reset"),
    path("password_reset_done/", auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path("reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path("reset_complete/", auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
]