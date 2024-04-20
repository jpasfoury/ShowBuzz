from django.db import models
from django.contrib.auth.models import User

class TVShow(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    genre = models.CharField(max_length=100)
    release_year = models.IntegerField()

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    show = models.ForeignKey(TVShow, on_delete=models.CASCADE)
    rating_value = models.IntegerField()
