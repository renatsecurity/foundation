from django.urls import path
from . import views

urlpatterns = [
    path('', views.past_programmes, name='past_programmes'),
]