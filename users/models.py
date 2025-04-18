from django.db import models
from django.contrib.auth.models import AbstractUser

from main.models import History, Song


# Create your models here.
class User(AbstractUser):
    image = models.ImageField(upload_to="users_img", blank=True, null=True, verbose_name="Аватар")
    email = models.EmailField(unique=True, blank=True, null=True)
    songs = models.ManyToManyField(Song)
    listened_songs = models.ManyToManyField(Song, through=History, related_name="listened_songs")
    
    class Meta:
        db_table = "users"
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.username