from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views

app_name = "App"

urlpatterns = [
    path("", views.index, name="index"),
    path("upload_song/", views.upload_song,name="upload_song"),
    #path("listOfSongs/", views.songList, name="songList"),
]