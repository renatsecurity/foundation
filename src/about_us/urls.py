from django.urls import path
from . import views

urlpatterns = [
    path('', views.about_us, name='about_us'),
    path('corporate-profile/', views.corporate_profile, name='about_corporate_profile'),
    path('corporate-profile/<slug:slug>/', views.corporate_profile_detail, name='about_corporate_profile_detail'),
]
