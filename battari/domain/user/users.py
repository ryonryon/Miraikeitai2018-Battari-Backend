from battari.models import Follow


class Users:
    def follows(self):
        follows = Follow.objects.filter(follower_user_id=self.my_spotify_id)
        if follows is None:
            return False
        else:
            return True

    def follower(self):
        follower = Follow.objects.filter(follower_user_id=self.spotify_id).count()
        return follower

    def following(self):
        following = Follow.objects.filter(following_user_id=self.spotify_id).count()
        return following

    def __init__(self, user, data):
        self.my_spotify_id = user["spotify_id"]
        self.spotify_id = data["spotify_id"]
