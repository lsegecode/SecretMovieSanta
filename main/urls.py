from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_list, name='movie_list'),  # Homepage showing all movies
]
