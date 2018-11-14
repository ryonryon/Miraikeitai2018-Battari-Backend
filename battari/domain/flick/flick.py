from battari.data.spotify.spotify import Spotify


class Flick:
    def track_detail(self):
        spotify = Spotify()
        track = spotify.get_track(self.track_id)

        return ""

    def __init__(self, data):
        self.track_id = data["track_id"]
        self.user_id = data["user_id"]
        self.comment = data["comment"]
        track = self.track_detail()
