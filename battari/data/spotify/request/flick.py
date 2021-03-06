from rest_framework import serializers


class Flick(object):
    def __init__(self, to):
        self.to = to


class Notification(object):
    def __init__(self, title, body, click_action):
        self.title = title
        self.body = body
        self.click_action = click_action


class Data(object):
    def __init__(self, event_type, sent_from, track_id, user_id, message):
        self.event_type = event_type
        self.sent_from = sent_from
        self.track_id = track_id
        self.user_id = user_id
        self.message = message


class NotificationSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=40)
    body = serializers.CharField(max_length=100)
    click_action = serializers.CharField(max_length=5)


class DataSerializer(serializers.Serializer):
    event_type = serializers.CharField(max_length=7)
    sent_from = serializers.CharField(max_length=50)
    track_id = serializers.CharField(max_length=30)
    user_id = serializers.CharField(max_length=50)
    message = serializers.CharField(max_length=200)


class FlickSerializer(serializers.Serializer):
    to = serializers.CharField(max_length=200)
    notification = NotificationSerializer()
    data = DataSerializer()
