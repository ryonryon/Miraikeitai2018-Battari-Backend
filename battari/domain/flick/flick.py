import json

from battari.data.firebase import Firebase
from battari.data.spotify.request.flick import Flick as SpotifyFlick
from battari.data.spotify.request.flick import Notification, Data
from battari.data.spotify.spotify import Spotify
from battari.models import User


class Flick:
    def __notification(self):
        track = self.__track_detail()
        title = self.user.displayname + "さんから曲が送られてきました"
        body = track["name"] + " - " + track["album"]["artists"][0]["name"]
        click_action = "PUSH"
        notification = Notification(title, body, click_action)
        return notification

    def __data(self):
        event_type = "flick"
        sent_from = self.user.displayname
        track_id = self.track_id
        message = self.comment
        user_id = self.user.spotify_id
        data = Data(event_type, sent_from, track_id, user_id, message)
        return data

    def __user(self):
        user = User.objects.get(spotify_id=self.user_id)
        return user

    def __json(self):
        to = self.__user().firebase_token
        notification = self.__notification().__dict__
        data = self.__data().__dict__
        flick = SpotifyFlick(to).__dict__
        flick["notification"] = notification
        flick["data"] = data
        flick = json.dumps(flick, sort_keys=True, ensure_ascii=False, indent=2).replace("\\", "")
        return flick

    def __track_detail(self):
        spotify = Spotify()
        track = spotify.get_track(self.track_id)
        return track

    def firebase(self):
        json = self.__json()
        Firebase().flick_notify(json)

    def __init__(self, data, user):
        self.track_id = data["track_id"]
        self.user_id = data["user_id"]
        self.comment = data["comment"]
        self.user = user
