from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


"""class User(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    email = models.CharField(max_length=400)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    rating = models.IntegerField(default=0)
"""


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    caption = models.CharField(max_length=200)
    image = models.FileField(upload_to='images/')
    text = models.TextField()
    comments = []
    rating = models.IntegerField(default=0)
    date = models.DateField(default=timezone.now())


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.CharField(max_length=2000)
    date = models.DateField()

    rating = models.IntegerField(default=0)
