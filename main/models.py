from django.contrib.auth.models import User
from django.db import models
#from main.models import movie


class Board(models.Model):
    title = models.CharField(max_length=20, null=True)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)

class Post(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()

class movie(models.Model):
    movie_Title = models.CharField(max_length=50)
    movie_Year = models.CharField(max_length=20)

class genre(models.Model):
    genre_title = models.CharField(max_length=50)
    genre_name = models.CharField(max_length=20)  



    def __str__(self):
        return self.text
