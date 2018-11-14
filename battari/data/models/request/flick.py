from rest_framework import serializers


class Flick(object):
    def __init__(self, track_id, user_id, comment):
        self.track_id = track_id
        self.user_id = user_id
        self.comment = comment


class FlickSerializer(serializers.Serializer):
    track_id = serializers.CharField(max_length=50)
    user_id = serializers.CharField(max_length=30)
    comment = serializers.CharField(max_length=200)
