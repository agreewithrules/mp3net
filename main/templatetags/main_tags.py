from django import template
from ..models import History


register = template.Library()

@register.simple_tag()
def date_listened(song_id, user_id):
    return History.objects.get(song_id=song_id, user_id=user_id).date_listened

@register.inclusion_tag("song.html")
def show_song(song):
    return {"song": song}