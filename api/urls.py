from django.urls import path
from . import views


app_name = "api"
urlpatterns = [
    path("add_song", views.add_song, name="add_song"),
    path("get_audio/<int:id>", views.get_audio, name="get_audio"),
    path("save_volume", views.save_volume, name="save_volume"),
]
