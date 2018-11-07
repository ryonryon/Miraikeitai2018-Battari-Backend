from rest_framework import serializers


class Login(object):
    def __init__(self, username, password):
        self.username = username
        self.password = password


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=30)
    password = serializers.CharField(max_length=20)
