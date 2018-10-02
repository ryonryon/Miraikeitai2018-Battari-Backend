from django.db import models
from django.contrib.auth.models import AbstractBaseUser


# Create your models here.
class User(models.Model):
    id = models.BigIntegerField()
    displayname = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    salt = models.CharField(max_length=10)
    icon = models.ImageField(null=True)
    current_listening_track = models.CharField()
    comment = models.CharField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Location(models.Model):
    id = models.BigIntegerField()
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    updated_at = models.DateTimeField(auto_now=True)


class Follow(models.Model):
    id = models.BigIntegerField()
    following_user_id = models.BigIntegerField()
    follower_user_id = models.BigIntegerField()


class Artist(models.Model):
    id = models.BigIntegerField()
    Spotify_id = models.BigIntegerField()
    name = models.CharField(max_length=100)


class Track(models.Model):
    id = models.BigIntegerField()
    spotify_id = models.BigIntegerField()
    name = models.CharField(max_length=255)
    player_url = models.TextField()


class Album(models.Model):
    id = models.BigIntegerField()
    spotify_id = models.BigIntegerField()
    name = models.CharField(max_length=255)
    release_date = models.DateTimeField(auto_now_add=True)