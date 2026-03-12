from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    poster = models.ImageField(upload_to='posters/')
    banner = models.ImageField(upload_to='banners/', blank=True, null=True)
    stream_link = models.URLField(max_length=500)
    download_link = models.URLField(max_length=500)
    release_date = models.DateField()
    is_trending = models.BooleanField(default=False)
    is_new = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
