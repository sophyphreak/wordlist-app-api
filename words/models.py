from django.db import models
from django.contrib.auth.models import User


class Word(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    word = models.CharField(max_length=50)
    times_seen = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.word
