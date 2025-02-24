from django.urls import path
from . import views

app_name = 'impact'

urlpatterns = [
    path('', views.impact_list, name='impact_list'),
    # path('<slug:slug>/', views.impact_detail, name='impact_detail'),
    path('country-chart-data/', views.country_chart_data, name="country_chart_data"),
    path('category-chart-data/', views.category_chart_data, name="category_chart_data"),
]