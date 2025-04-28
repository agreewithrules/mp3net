from django.shortcuts import render
from django.contrib.auth.decorators import login_required 
from django.core.paginator import Paginator
from django.contrib.postgres.search import SearchVector

from .forms import SupportForm
from .models import Song
from users.models import User


# Create your views here.
def home(request):
    songs = Song.objects.order_by("-id")

    context = {
        "title": "Home",
        "songs": songs,
    }
    return render(request, "main/home.html", context)

@login_required
def statistics(request):
    return render(request, "main/statistics.html", {"statistic": request.user.statistic})

@login_required
def support(request):
    if request.method == "POST":
        form = SupportForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = SupportForm()

    context = {
        "title": "Support",
        "form": form,
    }

    return render(request, "main/support.html", context)

@login_required
def favourites(request):
    user = User.objects.get(pk=request.user.id)
    if user:
        user_songs = user.songs.all()
    return render(request, "main/favourites.html", {"title": "Favourites", "user_songs": user_songs})

@login_required
def history(request):
    number = request.GET.get("page", 1)

    history = request.user.listened_songs.order_by("-history__date_listened")
    paginator = Paginator(history, 5)

    songs = paginator.page(number)
    return render(request, "main/history.html", {"songs": songs})

def search(request):
    query = request.POST.get("search", None)
    
    if query:
        songs = Song.objects.annotate(search=SearchVector("name", "artist"),).filter(search=query)
    else:
        songs = []

    context = {
        "title": "Home",
        "songs": songs,
    }
    return render(request, "main/home.html", context)