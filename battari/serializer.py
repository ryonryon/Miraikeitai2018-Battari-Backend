from rest_framework import serializers

from .models import User, Location, Follow, Artist, Track, Album


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'displayname')


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
