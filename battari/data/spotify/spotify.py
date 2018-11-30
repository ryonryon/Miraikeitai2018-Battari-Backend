import json
import urllib.parse
import urllib.request


class Spotify:
    def __get_token(self):
        url = 'https://accounts.spotify.com/api/token'

        authorization = "Basic " + self.key
        headers = {'Authorization': authorization}
        values = {"grant_type": "client_credentials"}
        data = urllib.parse.urlencode(values)
        data = data.encode('ascii')
        req = urllib.request.Request(url, data, headers)
        with urllib.request.urlopen(req) as res:
            return json.load(res)

    def get_track(self, track_id):
        url = "https://api.spotify.com/v1/tracks/" + track_id
        token = self.__get_token()
        authorization = "Bearer " + token["access_token"]
        headers = {'Authorization': authorization}
        req = urllib.request.Request(url=url, headers=headers)
        with urllib.request.urlopen(req) as res:
            return json.load(res)

    def __init__(self):
        self.key = "MDZlYmFkNjRmMTNiNGE5ZGFlNzdmNGQ4MWQ3OTk2ZTU6MWUyZWNhZTNlOWJhNDAyMGIzMzY5M2JiZDVkMWUyMmQ="
