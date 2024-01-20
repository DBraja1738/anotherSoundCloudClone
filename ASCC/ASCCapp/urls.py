from django.urls import path
from . import views
from musicPlayer import views as mPlayerV

urlpatterns=[
    path("",views.home, name="home"),
    path("listOfSongs/", mPlayerV.songList, name="songList"),
]