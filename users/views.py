from hashlib import file_digest
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse

from .forms import LoginForm, RegistrationUserForm, ProfileForm


# Create your views here.
def login(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = auth.authenticate(request, username=username, password=password)
            if user:
                auth.login(request, user)
                if request.POST.get("next", None):
                    return redirect(request.POST.get("next", None))

                return redirect("main:home")
    else:
        form = LoginForm()
        
    return render(request, "users/login.html", {"title": "Log in", "form": form,})

def registration(request):
    if request.method == "POST":
        form = RegistrationUserForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = form.instance
            auth.login(request, user)
            return redirect("main:home")
    else:
        form = RegistrationUserForm()

    context = {
        "title": "Registration",
        "form": form,
    }
    return render(request, "users/registration.html", context)

@login_required
def logout(request):
    auth.logout(request)
    return redirect(reverse("main:home"))

@login_required
def profile(request):
    if request.method == "POST":
        form = ProfileForm(data=request.POST, instance=request.user, files=request.FILES) # files=request.FILES
        if form.is_valid():
            form.save()
            return redirect("users:profile")
    else:
        form = ProfileForm(instance=request.user)

    context = {
        "title": "Profile",
        "form": form,
    }
    return render(request, "users/profile.html", context)
