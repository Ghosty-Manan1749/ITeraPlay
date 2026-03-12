from django.urls import path
from . import views

urlpatterns = [
    path('movie/<int:id>/', views.movie_links, name='movie_links'),
]
