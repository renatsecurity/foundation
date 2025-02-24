from django.urls import path
from .views import (
    news_list, news_detail,
    press_release_list, press_release_detail,
    podcast_list, podcast_detail
)

app_name = 'media_app'

urlpatterns = [
    path('news/', news_list, name='news_list'),
    path('news/<slug:slug>/', news_detail, name='news_detail'),

    path('press-releases/', press_release_list, name='press_release_list'),
    path('press-releases/<slug:slug>/', press_release_detail, name='press_release_detail'),

    path('podcasts/', podcast_list, name='podcast_list'),
    path('podcasts/<slug:slug>/', podcast_detail, name='podcast_detail'),
]
