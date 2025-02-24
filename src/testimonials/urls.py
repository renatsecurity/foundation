from django.urls import path
from . import views

urlpatterns = [
    path('', views.testimonials_list, name="testimonials_list"),
    path('<slug:slug>/', views.testimonial_detail, name="testimonial_detail"),
]