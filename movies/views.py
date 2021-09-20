from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from .models import Movie

# Create your views here.
def index(request):
    movies = Movie.objects.all()
    #output = ', '.join([m.title for m in movies])
    return render(request, 'movies/index.html', { 'movies': movies })

def detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)  #id or pk can be used either
    return render(request, 'movies/detail.html', { 'movie': movie })