from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    email=models.EmailField(max_length=100, unique=True)

class Post(models.Model):
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    title=models.CharField(max_length=2000)
    content=models.TextField()

class Comment(models.Model):
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    post=models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment')  #중첩 시리얼라이저 
    created_at=models.DateTimeField(auto_now_add=True)
    content=models.TextField()