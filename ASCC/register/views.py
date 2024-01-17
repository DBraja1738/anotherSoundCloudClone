from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate
from .forms import RegisterForm
# Create your views here.
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")  # Redirect to home after successful registration
    else:
        form = RegisterForm()

    return render(request, "register/register.html", {"form": form})