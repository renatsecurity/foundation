from django.urls import path
from . import views

urlpatterns = [
    path('', views.about_us, name='about_us'),
    path('mission-vision/', views.mission_vision, name='about_mission_vision'),
    path('mission-vision/<slug:slug>/', views.mission_vision, name='about_mission_vision'),
    path('corporate-profile/', views.corporate_profile, name='about_corporate_profile'),
    path('corporate-profile/<slug:slug>/', views.corporate_profile, name='about_corporate_profile'),
    path('partners/', views.partners_list, name='about_partners'),
    path('partners/<slug:slug>/', views.partner_detail, name='about_partner_detail'),
    path('mentors/', views.mentor_list, name='about_mentors'),
    path('mentors/<slug:slug>/', views.mentor_detail, name='about_mentor_detail'),
    path('get-involved/', views.get_involved, name='about_get_involved'),
    path('get-involved/<slug:slug>/', views.get_involved_detail, name='about_get_involved'),
    path('upcoming-events/', views.upcoming_events, name='about_upcoming_events'),
    path('upcoming-events/<slug:slug>/', views.upcoming_event_detail, name='about_upcoming_event_detail'),
]
