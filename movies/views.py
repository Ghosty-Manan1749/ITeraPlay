from django.shortcuts import render
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
