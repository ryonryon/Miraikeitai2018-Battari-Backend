from rest_framework import serializers


class TrackId(object):
    def __init__(self, track_id):
        self.track_id = track_id


class TrackSerializer(serializers.Serializer):
    track_id = serializers.CharField(max_length=50)
