from rest_framework import serializers


class Register(object):
    def __init__(self, user_id, displayname, password):
        self.user_id = user_id
        self.displayname = displayname
        self.password = password


class RegisterSerializer(serializers.Serializer):
    user_id = serializers.CharField(max_length=30)
    displayname = serializers.CharField(max_length=20)
    password = serializers.CharField(max_length=20)
