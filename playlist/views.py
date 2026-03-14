from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .play_list import Playlist
# Create your views here.

playlist = Playlist()

@api_view(['POST'])
def add_song(request):
    song = request.data.get("song")

    if not song:
        return Response({"error": "Song name required"}, status=400)

    playlist.add_song(song)

    return Response({
        "message": "Song added",
        "playlist": playlist.show_playlist()
    })
    

@api_view(['GET'])
def show_playlist(request):

    return Response({
        "playlist": playlist.show_playlist()
    })