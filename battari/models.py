from django.db import models
from django.contrib.auth.models import AbstractBaseUser


# Create your models here.
class User(models.Model):
    id = models.BigIntegerField(primary_key=True)
    displayname = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    salt = models.CharField(max_length=10)
    icon = models.ImageField(null=True)
    current_listening_track = models.CharField(max_length=30)  # max_lengthは仮設定(中身がわからないので半分放棄した)
    comment = models.CharField(max_length=30, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Location(models.Model):
    id = models.BigIntegerField(primary_key=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    updated_at = models.DateTimeField(auto_now=True)


class Follow(models.Model):
    id = models.BigIntegerField(primary_key=True)
    following_user_id = models.BigIntegerField()
    follower_user_id = models.BigIntegerField()


class Artist(models.Model):
    id = models.BigIntegerField(primary_key=True)
    Spotify_id = models.BigIntegerField()
    name = models.CharField(max_length=100)


class Track(models.Model):
    id = models.BigIntegerField(primary_key=True)
    spotify_id = models.BigIntegerField()
    name = models.CharField(max_length=255)
    player_url = models.TextField()


class Album(models.Model):
    id = models.BigIntegerField(primary_key=True)
    spotify_id = models.BigIntegerField()
    name = models.CharField(max_length=255)
    release_date = models.DateTimeField(auto_now_add=True)