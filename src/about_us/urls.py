from django.urls import path
from . import views

urlpatterns = [
    path('', views.about_us, name='about_us'),
    path('corporate-profile/', views.corporate_profile, name='about_corporate_profile'),
    path('export_corporate_profile_to_pdf/', views.export_corporate_profile_to_pdf, name='export_corporate_profile_to_pdf'),
]
