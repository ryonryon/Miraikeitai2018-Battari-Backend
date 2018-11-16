from battari.data.spotify.spotify import Spotify
from battari.models import User


class Flick:
    def __notification(self):
        return

    def __user(self):
        user = User.objects.get(user_id=self.user_id)
        return user

    def __data(self):
        return

    def track_detail(self):
        spotify = Spotify()
        track = spotify.get_track(self.track_id)
        return track

    def __init__(self, data, user):
        self.track_id = data["track_id"]
        self.user_id = data["user_id"]
        self.comment = data["comment"]
        self.user = user
        track = self.track_detail()
