from django.urls import path
from . import views

urlpatterns = [
    path('', views.mentor_list, name='mentor_list'),
    path('<slug:slug>/', views.mentor_detail, name='mentor_detail'),
]