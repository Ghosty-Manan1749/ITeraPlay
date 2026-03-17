from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)

    poster = models.ImageField(upload_to="posters/")
    banner = models.ImageField(upload_to="banners/", blank=True, null=True)

    movie_file = models.FileField(upload_to="movies/", blank=True, null=True)

    stream_link = models.URLField(blank=True, null=True)
    download_link = models.URLField(blank=True, null=True)

    release_date = models.DateField(blank=True, null=True)

    is_trending = models.BooleanField(default=False)
    is_new = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title