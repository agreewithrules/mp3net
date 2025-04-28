from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver

from main.models import History, Song, Statistic


# Create your models here.
class User(AbstractUser):
    image = models.ImageField(upload_to="users_img", blank=True, null=True, verbose_name="Аватар")
    email = models.EmailField(unique=True, blank=True, null=True)
    songs = models.ManyToManyField(Song)
    listened_songs = models.ManyToManyField(Song, through=History, related_name="listened_songs")
    statistic = models.OneToOneField(Statistic, on_delete=models.CASCADE, related_name='user_stat', null=True, blank=True)
    
    class Meta:
        db_table = "users"
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.username
    

@receiver(post_save, sender=User)
def create_stat(sender, instance, created, **kwargs):
    if created:
        stat = Statistic.objects.create()
        instance.statistic = stat
        instance.save()
