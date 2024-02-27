from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views



urlpatterns = [

    path("upload_song/", views.upload_song,name="upload_song"),
    path("play-song/<int:song_id>/", views.play_song, name="play_song"),
    path("play_playlist/<int:playlist_id>/", views.play_playlist, name="play_playlist")
    
]