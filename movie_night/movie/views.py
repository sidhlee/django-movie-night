from django.shortcuts import render
import requests


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

# Create your views here.
def _get_movies(search_string="time"):
    """
    get 10 movies with the given search string.
    TODO: add pagination option
    """
    api_key = "2610afcc"
    # https://pypi.org/project/requests/
    movies_response = requests.get(
        f"https://omdbapi.com/?s={search_string}&apikey={api_key}"
    )
    movies_dict = movies_response.json()
    movies_list = movies_dict.get("Search", [])
    return movies_list


def index(request):
    """
    Renders html inside templates folder
    """
    context = {}
    # movies = _get_movies()
    movies = TEST_MOVIES
    context["movies"] = movies
    print(movies)

    return render(request, "movies/index.html", context)
