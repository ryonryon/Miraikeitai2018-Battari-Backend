from battari.models import Follow


class User:
    def count_follows(self, spotify_id):
        followers = Follow.objects.filter(follower_user_id=spotify_id).count()
        followings = Follow.objects.filter(following_user_id=spotify_id).count()

        self.user.firebase_token = token
        self.user.save()

    def __init__(self, user):
        self.user = user
