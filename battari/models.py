from django.db import models
from django.contrib.auth.models import AbstractBaseUser


# Create your models here.
class User(models.Model):
    id = models.BigIntegerField(primary_key=True)
    displayname = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    salt = models.CharField(max_length=10)
    icon = models.TextField()
    current_listening_track = models.CharField(max_length=30)
    comment = models.CharField(max_length=30, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Location(models.Model):
    id = models.BigIntegerField(primary_key=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Map(models.Model):
    id = models.BigIntegerField(primary_key=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    spotify_id = models.CharField(max_length=30)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Follow(models.Model):
    id = models.BigIntegerField(primary_key=True)
    following_user_id = models.BigIntegerField()
    follower_user_id = models.BigIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)


class Notification(models.Model):
    id = models.BigIntegerField(primary_key=True)
    receive_user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)


class UserAction(models.Model):
    id = models.BigIntegerField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
