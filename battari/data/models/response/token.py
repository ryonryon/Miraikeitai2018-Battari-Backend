from rest_framework import serializers


class Token(object):
    def __init__(self, token):
        self.token = token


class TokenSerializer(serializers.Serializer):
    token = serializers.CharField(max_length=200)
