from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Rating(models.Model):
    movie = models.ForeignKey("Movie", on_delete=models.CASCADE)
    source = models.CharField(max_length=200)
    value = models.CharField(max_length=200)


class Movie(models.Model):
    title = models.CharField(max_length=200)
    year = models.CharField(max_length=200)
    rated = models.CharField(max_length=200)
    released = models.CharField(max_length=200)
    runtime = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    director = models.CharField(max_length=200)
    writer = models.CharField(max_length=200)
    actors = models.CharField(max_length=200)
    plot = models.TextField(max_length=1000)
    language = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    awards = models.CharField(max_length=200)
    poster = models.URLField()
    metascore = models.IntegerField()
    imdb_rating = models.DecimalField(max_digits=3, decimal_places=1)
    imdb_votes = models.CharField(max_length=200)
    imdb_id = models.CharField(max_length=200)
    # TODO: use enum
    type = models.CharField(max_length=200)
    dvd = models.CharField(max_length=200)
    box_office = models.CharField(max_length=200)
    production = models.CharField(max_length=200)
    website = models.CharField(max_length=200)
    response: models.BooleanField()


class UserMovie(models.Model):
    """Through table for each users favorite movies"""

    user = models.ForeignKey(
        User, related_name="favorite_movies", on_delete=models.CASCADE
    )
    movie = models.ForeignKey(Movie, related_name="users", on_delete=models.DO_NOTHING)
