# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from . models import Song, Playlist, Comment, Like
from .forms import SongUploadForm, SongSearchForm, CommentForm



@login_required(login_url='login')
def upload_song(request):
    if request.method == 'POST':
        form = SongUploadForm(request.POST, request.FILES)
        if form.is_valid():
            song = form.save(commit=False)
            song.user = request.user  
            song.save()
            return redirect('home')  
    else:
        form = SongUploadForm()

    return render(request, 'upload_song.html', {'form': form})

def songList(request):
    songs=Song.objects.all()
    return render(request,"listSongs.html",{"songs" : songs})

def play_song(request,song_id):
    song = get_object_or_404(Song, pk=song_id)
    comments=Comment.objects.filter(song=song)
    user=request.user

    if not request.user.is_authenticated:
        return render(request, 'play_song.html', {'song': song, "comments" : comments})

    user_has_liked = Like.objects.filter(user=user, song=song).exists()

    if request.method=="POST":
        form=CommentForm(request.POST)

        if 'like' in request.POST:
            
            if user_has_liked:
                song.likes -= 1
                Like.objects.filter(user=user, song=song).delete()
            else:
                song.likes += 1
                Like.objects.create(user=user, song=song)

            song.save()

        elif 'comment' in request.POST:
            
            if form.is_valid():
                new_comment_text = form.cleaned_data["text"]
                Comment.objects.create(user=user, song=song, body=new_comment_text)

        return redirect('play_song', song_id=song_id)
    else:
        form=CommentForm()
    song.listen_count += 1
    song.save()

 

    return render(request, 'play_song.html', {'song': song, "comments" : comments, "form" : form , 'user_has_liked': user_has_liked})


def create_playlist(request):
    if request.method=="POST":
        playlist_name=request.POST.get("playlist_name")
        song_ids=request.POST.getlist("songs")

        playlist = Playlist.objects.create(user=request.user, name=playlist_name)
        playlist.songs.add(*song_ids)
    
    songs=Song.objects.all()

    return render(request, "create_playlist.html", {"songs" : songs})

def songSearch(request):
    if request.method=="POST":
        form=SongSearchForm(request.POST)
        if form.is_valid():
            searchQuery=form.cleaned_data["searchQuery"]
            songs=Song.objects.filter(title__icontains=searchQuery)
        else:
            songs=Song.objects.all()
    else:
        form=SongSearchForm()
        songs=None
    return render(request, "searchSong.html", {"form":form , "songs":songs})

def profileView(request):
    user=request.user
    songs=Song.objects.filter(user=user)
    playlists=Playlist.objects.filter(user=user)

    return render(request,"profileView.html",{"songs" : songs, "playlists" : playlists})