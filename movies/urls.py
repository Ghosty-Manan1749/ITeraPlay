from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_list, name='movies'),
    path('category/<int:category_id>/', views.category_movies, name='category_movies'),
    path('links/<int:movie_id>/', views.movie_links, name='movie_links'),
]
