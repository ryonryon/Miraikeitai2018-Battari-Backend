from django.db import models
from django.contrib.auth.models import AbstractBaseUser


# Create your models here.
class User(models.Model):
    displayname = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    salt = models.CharField(max_length=10)
    icon = models.ImageField(null=True)
    current_listening_track = models.CharField()
    comment = models.CharField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
