from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()  # short movie description
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    poster = models.ImageField(upload_to='posters/')
    movie_file = models.FileField(upload_to='movies/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
