from django.urls import path
from . import views

urlpatterns = [
    path('', views.research_list, name='research_list'),
    path('<slug:slug>/', views.research_detail, name='research_detail'),
    path('category/<slug:slug>/', views.research_category_detail, name='research_category_detail'),
]