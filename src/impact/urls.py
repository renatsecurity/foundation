from django.urls import path
from . import views

app_name = 'impact'

urlpatterns = [
    path('', views.impact_list, name='impact_list'),
    path('<slug:slug>/', views.impact_detail, name='impact_detail'),
]