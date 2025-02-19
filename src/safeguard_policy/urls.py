from django.urls import path
from . import views

urlpatterns = [
    path('', views.policy_list, name='safeguard_policy_list'),
    path('<int:id>/', views.policy_detail, name='safeguard_policy_detail'),
]
