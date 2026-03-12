from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Movie

@login_required(login_url='login')
def movie_links(request, id):
    movie = get_object_or_404(Movie, id=id)
    return render(request, 'movies/movie_links.html', {'movie': movie})
