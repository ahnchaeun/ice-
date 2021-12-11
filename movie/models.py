from django.db import models

class movie(models.Model):
    movie_ID = models.CharField(max_length = 20)
    movie_Title = models.CharField(max_length= 50)
    movie_Year = models.CharField(max_length = 20)

    def __str__(self):
        return self.text
    
