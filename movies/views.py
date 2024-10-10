from django.shortcuts import render
from .models import Movie

# Create your views here.
def movie_list(request):
    # Query all movies from the Movie model
    movies = Movie.objects.all()

    # Pass the movies to the 'movies_list.html' template
    return render(request, 'movies_list.html', {'movies': movies})