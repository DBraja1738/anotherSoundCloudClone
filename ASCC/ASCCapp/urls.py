from django.urls import path
from . import views
from musicPlayer import views as mPlayerV
from django.contrib.auth import views as authV

urlpatterns=[
    path("",views.home, name="home"),
    path("listOfSongs/", mPlayerV.songList, name="songList"),
    path("createPlaylist/",mPlayerV.create_playlist, name="createPlaylist"),
    path("uploadSong/",mPlayerV.upload_song, name="uploadSong"),
    path("songSearch/",mPlayerV.songSearch, name="songSearch"),
    path('logout/', authV.LogoutView.as_view(), name='logout'),
]