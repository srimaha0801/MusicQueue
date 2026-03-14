from django.urls import path
from .views import add_song, show_playlist

urlpatterns = [
    path('add-song/', add_song),
    path('playlist/', show_playlist),
]