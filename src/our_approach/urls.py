from django.urls import path
from . import views

urlpatterns = [
    path('', views.our_approach_list, name='our_approach_list'),
    path('<slug:slug>/', views.our_approach_detail, name='our_approach_detail'),
]
