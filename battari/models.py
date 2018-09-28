from django.db import models
from django.contrib.auth.models import AbstractBaseUser


# Create your models here.
class User(models.Model):
    id = models.CharField()
    battari_id = models.CharField()
    username = models.CharField(max_length=30)
    displayname = models.CharField(max_length=30)
    password = models.CharField() #  ソルトは未考慮・・・というかどこに持たせれば良いのかわからない
    icon = models.ImageField(null=True)
    current_listening_track = models.CharField()
    comment = models.CharField(null=True)
    follower = models.IntegerField()
    following = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
