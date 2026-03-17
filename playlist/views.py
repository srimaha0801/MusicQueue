from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .play_list import Playlist
# Create your views here.
# {"song":""}
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
def play_song(request):
    song = request.data.get('song')
    return Response({
        "playlist": playlist.play_song(song)
    })

@api_view(['GET'])
def show_playlist(request):
    return Response({
        "playlist": playlist.show_playlist()
    })

@api_view(['POST'])
def next_song(request):
    song = request.data.get("song")
    if not song:
        return Response({"error": "Song name required"}, status=400)
    
    return Response({"Next song" : playlist.next_song(song)})

@api_view(['POST'])
def prev_song(request):
    song = request.data.get("song")
    return Response({
        "Previous song": playlist.prev_song(song)
    })

@api_view(['DELETE'])
def delete_song(request,song):
    # song = request.GET.get("song")
    return Response({
        "message":playlist.delete_song(song)
    })