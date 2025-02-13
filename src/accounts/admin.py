from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from simple_history.admin import SimpleHistoryAdmin
from .models import CustomUser, UserActivity


class CustomUserAdmin(UserAdmin, SimpleHistoryAdmin):
    model = CustomUser
    list_display = ["username", "email", "role", "is_active", "date_joined"]
    list_filter = ["role", "is_active"]
    history_list_display = ["role", "is_active"]
    search_fields = ["username", "email"]
    ordering = ["date_joined", 'username']
    fieldsets = (
        (None, {"fields": ("username", "first_name", "last_name", "email", "password")}),
        ("Personal Info", {"fields": ("phone_number", "profile_picture", "bio")}),
        ("Permissions", {"fields": ("role", "is_active", "is_staff", "is_superuser")}),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )


@admin.register(UserActivity)
class UserActivityAdmin(admin.ModelAdmin):
    list_display = ("user", "action", "ip_address", "timestamp")
    list_filter = ("action", "timestamp")
    search_fields = ("user__username", "ip_address")


admin.site.register(CustomUser, CustomUserAdmin)