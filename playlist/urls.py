from django.urls import path
from .views import add_song, show_playlist,next_song,prev_song,play_song,delete_song

urlpatterns = [
    path('add-song/', add_song),
    path('playlist/', show_playlist),
    path('next-song/', next_song),
    path('prev_song/', prev_song),
    path('play_song/', play_song),
    path('delete_song/<str:song>',delete_song)
]