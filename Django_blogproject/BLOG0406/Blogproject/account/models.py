from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class CustomUser(AbstractUser): #상속
    nickname=models.CharField(max_length=100)
    university=models.CharField(max_length=50)
    location=models.CharField(max_length=200)