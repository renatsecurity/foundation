from django.urls import path
from . import views

urlpatterns = [
    path('', views.terms_and_conditions, name='terms_and_conditions'),
]