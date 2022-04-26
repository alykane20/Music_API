
from django.db import models

    

class Song(models.Model):
    title = models.CharField(max_length=250)
    artist = models.CharField(max_length=250)
    album = models.CharField(max_length=250)
    release_date = models.DateField()
    genre = models.CharField(max_length=300)
    likes = models.IntegerField(default=0)

