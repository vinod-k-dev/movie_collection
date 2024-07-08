from django.db import models
from django.contrib.auth.models import User
import uuid

class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    genres = models.CharField(max_length=255)
    uuid = models.UUIDField(unique=True, default=uuid.uuid4)

    def __str__(self):
        return f"{self.title}"


class Collection(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    movies = models.ManyToManyField(Movie)
    uuid = models.UUIDField(unique=True, default=uuid.uuid4)

    def __str__(self):
        return f"{self.user} - {self.title}"
