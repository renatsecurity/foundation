from django.urls import path
from . import views


app_name ='media_app'

urlpatterns = [
    path('', views.media_list, name='media_list'),
    path('<slug:slug>/', views.media_detail, name='media_detail'),
    path('type/<slug:media_type>/', views.media_type_list, name='media_type_list'),
]
