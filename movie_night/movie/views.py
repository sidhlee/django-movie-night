from django.shortcuts import render

# Create your views here.


def index(request):
    ''' 
    Renders html inside templates folder
    '''

    context = {

    }
    return render(request, 'movies/index.html', context)
