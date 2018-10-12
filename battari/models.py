from django.db import models

from battari.util.big_auto_field import BigAutoField


class User(models.Model):
    id = BigAutoField(primary_key=True)
    spotify_id = models.CharField(max_length=30)
    displayname = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    salt = models.CharField(max_length=10)
    icon = models.TextField(default="")
    firebase_token = models.CharField(max_length=160)
    battari_token = models.CharField(max_length=50)
    current_listening_track = models.CharField(max_length=30)
    comment = models.CharField(max_length=30, null=True)
    updated_at = models.DateTimeField(auto_now=True)


class Location(models.Model):
    id = BigAutoField(primary_key=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    updated_at = models.DateTimeField(auto_now=True)


class Map(models.Model):
    id = BigAutoField(primary_key=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    spotify_id = models.CharField(max_length=30)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)


class Follow(models.Model):
    id = BigAutoField(primary_key=True)
    following_user_id = models.BigIntegerField()
    follower_user_id = models.BigIntegerField()


class Notification(models.Model):
    id = BigAutoField(primary_key=True)
    receive_user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=50)


class UserAction(models.Model):
    id = BigAutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
