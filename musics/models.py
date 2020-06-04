from django.db import models

class Song(models.Model):
    name = models.CharField(max_length=100)
    time = models.DateTimeField('date published')
    artists_id = models.IntegerField(default=0)
    album_id = models.IntegerField(default=0)
    genre = models.CharField(max_length=50)
    song_file = models.FileField(upload_to='songs')

def __str__(self):
    return self.name         
class Album(models.Model):
    name = models.CharField(max_length=50)
    genre = models.CharField(max_length=20)
    user_id = models.IntegerField(default=0)
    cover = models.ImageField(upload_to='covers')
    album_file = models.FileField(upload_to='albums')

def __str__(self):
    return self.name

class Organization(models.Model):
    location = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone_no = models.IntegerField(default='')
    address = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
