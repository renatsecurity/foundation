from django.urls import path
from . import views

urlpatterns = [
    path('', views.article_list, name='gender_and_green_list'),
    path('<slug:slug>/', views.article_detail, name='gender_and_green_detail'),
    path('category/<slug:slug>/', views.category_detail, name='gender_and_green_category_detail'),
]