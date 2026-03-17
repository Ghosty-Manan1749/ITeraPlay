from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Movie, Category

def movie_list(request):
    movies = Movie.objects.all()
    categories = Category.objects.all()

    return render(request, 'movies.html', {
        'movies': movies,
        'categories': categories
    })

def category_movies(request, category_id):
    movies = Movie.objects.filter(category_id=category_id)
    categories = Category.objects.all()

    return render(request, 'movies.html', {
        'movies': movies,
        'categories': categories
    })

@login_required(login_url='login')
def movie_links(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    return render(request, 'movies/movie_links.html', {'movie': movie})
