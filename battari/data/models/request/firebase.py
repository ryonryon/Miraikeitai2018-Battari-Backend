from rest_framework import serializers


class Firebase(object):
    def __init__(self, token):
        self.token = token


class FirebaseSerializer(serializers.Serializer):
    token = serializers.CharField(max_length=50)
