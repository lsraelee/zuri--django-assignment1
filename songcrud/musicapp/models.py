from django.db import models
from datetime import datetime

class Artiste(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    age = models.IntegerField(default= None)
    
    def __str__(self):
        return self.last_name + " " + self.first_name

class Song(models.Model):
    artiste_id  = models.ForeignKey(Artiste, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    date_released = models.DateField(default=datetime.today)
    likes = models.IntegerField(default=None)
    
    def __str__(self):
        return self.title
    

class Lyric(models.Model):
    song_id = models.ForeignKey(Song, on_delete=models.CASCADE)
    content = models.TextField(default=None)
    
    def __str__(self):
        return self.song

