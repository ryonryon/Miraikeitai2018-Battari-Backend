from battari.models import User
from battari.models import Follow


class Users:
    # def id(self):
    #     id = User.object.get()

    def follower(self):
        follower = Follow.objects.filter(follower_user_id=self.spotify_id).count()
        return follower

    def following(self):
        following = Follow.objects.filter(following_user_id=self.spotify_id).count()
        return following

    def __init__(self, spotify_id):
        self.spotify_id = spotify_id
