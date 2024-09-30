from django.shortcuts import render
from .models import Movie

# Example view that lists all movies
def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'movie_list.html', {'movies': movies})
