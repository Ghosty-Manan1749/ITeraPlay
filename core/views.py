from django.shortcuts import render
from movies.models import Movie

def home(request):
    movies = Movie.objects.all().order_by('-created_at')
    return render(request, 'core/home.html', {'movies': movies})
