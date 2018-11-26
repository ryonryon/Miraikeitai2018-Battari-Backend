from rest_framework import serializers


class Token(object):
    def __init__(self, id, displayname, follows, icon,
                 current_listening_track, comment, follower, following):
        self.id = id
        self.displayname = displayname
        self.follows = follows
        self.icon = icon
        self.current_listening_track = current_listening_track
        self.comment = comment
        self.follower = follower
        self.following = following



class TokenSerializer(serializers.Serializer):
    id = serializers.CharField(max_length=30),
    displayname = serializers.CharField(max_length=20),
    follows = serializers.BooleanField(),
    icon = serializers.CharField(),
    current_listening_track = serializers.CharField(max_length=30),
    comment = serializers.CharField(max_length=30, null=True),
    follower = serializers.IntegerField(),
    following = serializers.IntegerField()
