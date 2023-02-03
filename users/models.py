from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Person(AbstractUser):
    cin =models.CharField(primary_key=True,max_length=8)
    email = models.EmailField(unique=True)
    username = models.CharField(unique=True,max_length=40)
    USERNAME_FIELD ='username'
    