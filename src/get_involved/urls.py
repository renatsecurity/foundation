from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_involved_list, name='get_involved_list'),
    path('<slug:slug>/', views.get_involved_detail, name='get_involved_detail'),
    path('category/<slug:slug>/', views.get_involved_category_detail, name='get_involved_category_detail'),
]
