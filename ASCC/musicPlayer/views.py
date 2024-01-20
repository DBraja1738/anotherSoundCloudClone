# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from . models import Song
from .forms import SongUploadForm

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