from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from musicPlayer import models as musMod

def home(request):
    songs= musMod.Song.objects.all().order_by("listen_count")
    return render(request,"home.html",{"songs" : songs})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful.')
            return redirect('home')
        else:
            messages.error(request, 'Invalid login credentials.')

    return render(request, 'registration/login.html')


