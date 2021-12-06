from django.db import models

class Board(models.Model):
    title = models.CharField(max_length=20, null=True)
    content = models.TextField()
    writer = models.CharField(max_length=20, null=True)

class Post(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()


    def __str__(self):
        return self.text
