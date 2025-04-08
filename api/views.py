import json
from django.http import HttpResponse, JsonResponse
from users.models import User
from main.models import History, Song


# Create your views here.
def add_song(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    user = User.objects.get(id=body["user_id"])
    song = Song.objects.get(id=body["value"])
    if user and song:
        user.songs.add(song)
    return HttpResponse()


def get_audio(request, id):
    song = Song.objects.get(id=id)
    
    if request.user.is_authenticated and request.GET.get("addtohistory") != "false":
        History.objects.update_or_create(
            user=request.user,
            song=song,
        )

    # Добавить получение аудио из истории 
    if request.GET.get("favourites", None):
        songs = request.user.songs
        prev = songs.filter(pk__lt=id).last()
        next = songs.filter(pk__gt=id).first()
        request.session["fav_song_id"] = id
    else:
        prev = Song.objects.filter(pk__gt=id).first()
        next = Song.objects.filter(pk__lt=id).last()
        request.session["song_id"] = id




    data = {
        "song": {
            "id": id,
            "name": song.name,
            "artist": song.artist,
            "image": song.image.url,
            "audio": song.audio.url,
            },
        "prev": prev.id if prev else None,
        "next": next.id if next else None,
    }

    return JsonResponse(data)

def save_volume(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    value = body["volume"]
    if value:
        request.session["volume"] = value
    return HttpResponse()