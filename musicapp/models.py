from datetime import date
from django.db import models

# Create your models here.


class Artiste(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.IntegerField()


class Song (models.Model):
    Artiste = models.ForeignKey(Artiste, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    date_released = models.DateField(default=date.today)
    likes = models.IntegerField()
    artiste_id = models.IntegerField()


class Lyrics(models.Model):
    Song = models.ForeignKey(Song, on_delete=models.CASCADE)
    content = models.CharField(max_length=1000)
    song_id = models.IntegerField()
