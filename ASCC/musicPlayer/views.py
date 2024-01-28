# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from . models import Song, Playlist, Comment, Like
from .forms import SongUploadForm, SongSearchForm, CommentForm

def index(request):
    paginator= Paginator(Song.objects.all(),1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context={"page_obj":page_obj}
    return render(request,"index.html",context)

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

    user_has_liked = Like.objects.filter(user=user, song=song).exists()

    if request.method=="POST":
        form=CommentForm(request.POST)
        if user_has_liked:
            
            song.likes -= 1
            song.save()

           
            Like.objects.filter(user=user, song=song).delete()
        else:
           
            song.likes += 1
            song.save()

           
            Like.objects.create(user=user, song=song)

        if form.is_valid():
            newCommentText= form.cleaned_data["text"]
            Comment.objects.create(user=request.user, song=song, body=newCommentText)
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
        songs=Song.objects.all()
    return render(request, "searchSong.html", {"form":form , "songs":songs})