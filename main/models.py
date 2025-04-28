from django.db import models
from django.conf import settings


# Create your models here.
class Song(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    artist = models.CharField(max_length=100, verbose_name="Исполнитель")
    image = models.ImageField(upload_to="songs_img", verbose_name="Изображение")
    audio = models.FileField(upload_to="songs", verbose_name="Аудио")
    count = models.IntegerField(default=0)

    class Meta:
        db_table = "song"
        verbose_name = "Песня"
        verbose_name_plural = "Песни"

    def __str__(self):
        return f"{self.artist}: {self.name}"    


class Support(models.Model):
    username = models.CharField(max_length=150, verbose_name="Имя пользователя")
    email = models.EmailField()
    text = models.TextField()
    time_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "support"
        ordering = ["-time_created"]


class History(models.Model):
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_listened = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'history'


class Statistic(models.Model):
    added_to_favourites = models.IntegerField(default=0, verbose_name='Добавлено')

    class Meta:
        db_table = 'statistic'
