from django.shortcuts import render
import requests

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
    movies = _get_movies()
    context["movies"] = movies
    print(movies)

    return render(request, "movies/index.html", context)
