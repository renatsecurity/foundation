from django.urls import path
from . import views

urlpatterns = [
    path('', views.partner_list, name='partner_list'),
    path('<slug:slug>/', views.partner_detail, name='partner_detail'),
]