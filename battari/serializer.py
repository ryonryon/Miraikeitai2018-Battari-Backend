from rest_framework import serializers

from .models import User, Location, Map, Follow, Notification, UserAction


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'


class MapSerializer(serializers.ModelSerializer):
    class Meta:
        model = Map
        fields = '__all__'


class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model =Follow
        fields = '__all__'


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'


class UserActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAction
        fields = '__all__'
