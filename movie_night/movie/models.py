from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Movie(models.Model):
    imdb_id = models.CharField(max_length=200)
    title = models.CharField(max_length=200, null=True)
    poster = models.URLField(null=True)
    year = models.IntegerField(null=True)


class UserMovie(models.Model):
    """Through table for each users favorite movies"""

    user = models.ForeignKey(
        User, related_name="favorite_movies", on_delete=models.CASCADE
    )
    movie = models.ForeignKey(Movie, related_name="users", on_delete=models.CASCADE)
