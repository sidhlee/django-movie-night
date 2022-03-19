from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import requests
from .models import Movie, UserMovie


TEST_MOVIES = [
    {
        "Title": "Once Upon a Time... In Hollywood",
        "Year": "2019",
        "imdbID": "tt7131622",
        "Type": "movie",
        "Poster": "https://m.media-amazon.com/images/M/MV5BOTg4ZTNkZmUtMzNlZi00YmFjLTk1MmUtNWQwNTM0YjcyNTNkXkEyXkFqcGdeQXVyNjg2NjQwMDQ@._V1_SX300.jpg",
    },
    {
        "Title": "In Time",
        "Year": "2011",
        "imdbID": "tt1637688",
        "Type": "movie",
        "Poster": "https://m.media-amazon.com/images/M/MV5BMjA3NzI1ODc1MV5BMl5BanBnXkFtZTcwMzI5NjQwNg@@._V1_SX300.jpg",
    },
    {
        "Title": "Once Upon a Time in America",
        "Year": "1984",
        "imdbID": "tt0087843",
        "Type": "movie",
        "Poster": "https://m.media-amazon.com/images/M/MV5BMGFkNWI4MTMtNGQ0OC00MWVmLTk3MTktOGYxN2Y2YWVkZWE2XkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SX300.jpg",
    },
    {
        "Title": "About Time",
        "Year": "2013",
        "imdbID": "tt2194499",
        "Type": "movie",
        "Poster": "https://m.media-amazon.com/images/M/MV5BMTA1ODUzMDA3NzFeQTJeQWpwZ15BbWU3MDgxMTYxNTk@._V1_SX300.jpg",
    },
    {
        "Title": "No Time to Die",
        "Year": "2021",
        "imdbID": "tt2382320",
        "Type": "movie",
        "Poster": "https://m.media-amazon.com/images/M/MV5BYWQ2NzQ1NjktMzNkNS00MGY1LTgwMmMtYTllYTI5YzNmMmE0XkEyXkFqcGdeQXVyMjM4NTM5NDY@._V1_SX300.jpg",
    },
    {
        "Title": "Once Upon a Time in the West",
        "Year": "1968",
        "imdbID": "tt0064116",
        "Type": "movie",
        "Poster": "https://m.media-amazon.com/images/M/MV5BZGI5MjBmYzYtMzJhZi00NGI1LTk3MzItYjBjMzcxM2U3MDdiXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_SX300.jpg",
    },
    {
        "Title": "Prince of Persia: The Sands of Time",
        "Year": "2010",
        "imdbID": "tt0473075",
        "Type": "movie",
        "Poster": "https://m.media-amazon.com/images/M/MV5BMTMwNDg0NzcyMV5BMl5BanBnXkFtZTcwNjg4MjQyMw@@._V1_SX300.jpg",
    },
    {
        "Title": "Once Upon a Time",
        "Year": "2011–2018",
        "imdbID": "tt1843230",
        "Type": "series",
        "Poster": "https://m.media-amazon.com/images/M/MV5BNjBmZmI0ZDktODI2MS00MDU1LTk0NDYtNGE0MDc0OWVkYzcwXkEyXkFqcGdeQXVyMzAzNTY3MDM@._V1_SX300.jpg",
    },
    {
        "Title": "Hot Tub Time Machine",
        "Year": "2010",
        "imdbID": "tt1231587",
        "Type": "movie",
        "Poster": "https://m.media-amazon.com/images/M/MV5BMTQwMjExODA4Ml5BMl5BanBnXkFtZTcwNTYwMDYxMw@@._V1_SX300.jpg",
    },
    {
        "Title": "Once Upon a Time in Mexico",
        "Year": "2003",
        "imdbID": "tt0285823",
        "Type": "movie",
        "Poster": "https://m.media-amazon.com/images/M/MV5BMTU5MDg5OTcwOV5BMl5BanBnXkFtZTcwMjI1MTIzMw@@._V1_SX300.jpg",
    },
]

TEST_MOVIE = {
    "Title": "Once Upon a Time... In Hollywood",
    "Year": "2019",
    "Rated": "R",
    "Released": "26 Jul 2019",
    "Runtime": "161 min",
    "Genre": "Comedy, Drama",
    "Director": "Quentin Tarantino",
    "Writer": "Quentin Tarantino",
    "Actors": "Leonardo DiCaprio, Brad Pitt, Margot Robbie",
    "Plot": "A faded television actor and his stunt double strive to achieve fame and success in the final years of Hollywood's Golden Age in 1969 Los Angeles.",
    "Language": "English, Italian, Spanish, German",
    "Country": "United States, United Kingdom, China",
    "Awards": "Won 2 Oscars. 143 wins & 380 nominations total",
    "Poster": "https://m.media-amazon.com/images/M/MV5BOTg4ZTNkZmUtMzNlZi00YmFjLTk1MmUtNWQwNTM0YjcyNTNkXkEyXkFqcGdeQXVyNjg2NjQwMDQ@._V1_SX300.jpg",
    "Ratings": [
        {"Source": "Internet Movie Database", "Value": "7.6/10"},
        {"Source": "Rotten Tomatoes", "Value": "85%"},
        {"Source": "Metacritic", "Value": "83/100"},
    ],
    "Metascore": "83",
    "imdbRating": "7.6",
    "imdbVotes": "671,685",
    "imdbID": "tt7131622",
    "Type": "movie",
    "DVD": "27 Aug 2019",
    "BoxOffice": "$142,502,728",
    "Production": "N/A",
    "Website": "N/A",
    "Response": "True",
}

API_KEY = "2610afcc"

default_options = {"search": "time"}

# Create your views here.
def _get_movies(search_string="time"):
    """
    get 10 movies with the given search string.
    TODO:
        - add pagination option
        - add validation to search_string
    """
    api_key = "2610afcc"
    # https://pypi.org/project/requests/
    movies_response = requests.get(
        f"https://omdbapi.com/?s={search_string}&apikey={API_KEY}"
    )
    movies_dict = movies_response.json()
    movies_list = movies_dict.get("Search", [])
    return movies_list


def _get_movie_by_id(movie_id):
    """
    Get the movie by its imdbID
    TODO: validate args
    """
    params = {"i": movie_id, "apiKey": API_KEY}
    movie_response = requests.get("https://omdbapi.com/", params=params)
    movie_dict = movie_response.json()
    return movie_dict


def index(request):
    """
    Renders html inside templates folder.
    """
    context = {}
    # movies = _get_movies()
    movies = TEST_MOVIES
    context["movies"] = movies

    return render(request, "movies/index.html", context)


def movie_detail(request, movie_id):
    """
    Renders details with the given movie id.
    """
    context = {}
    if request.user.is_authenticated:
        user_movies = UserMovie.objects.filter(
            user=request.user, movie__imdb_id=movie_id
        )
        if user_movies:
            context["is_favorite"] = True

    movie = _get_movie_by_id(movie_id)
    context["movie"] = movie
    # movie = TEST_MOVIE

    return render(request, "movies/detail.html", context)


@login_required
def favorites(request, movie_id):
    # TODO: validate movie exists
    if request.method == "POST":
        movie = _get_movie_by_id(movie_id)
        movie_model = Movie.objects.create(
            imdb_id=movie_id,
            title=movie["Title"],
            poster=movie["Poster"],
            year=int(movie["Year"]),
        )
        UserMovie.objects.create(user=request.user, movie=movie_model)
        return render(
            request, "movies/detail.html", {"movie": movie, "is_favorite": True}
        )
    elif request.method == "GET":
        print("GET favorite movies")
        favorite_movies = UserMovie.objects.filter(user=request.user)
        context = {}
        context["movies"] = favorite_movies
        return render(request, "movies/favorites.html", context)
