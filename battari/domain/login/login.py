from django.core.exceptions import ObjectDoesNotExist

from battari.domain.login.password import Password
from battari.models import User


class Login:
    def token(self):
        password = Password(self.password)
        try:
            salt = User.objects.get(spotify_id=self.user_id).salt.encode()
            hashed_password = password.hashing(salt)
            user = User.objects.get(spotify_id=self.user_id, password=hashed_password)
        except ObjectDoesNotExist:
            return None

        return user.battari_token

    def __init__(self, data):
        self.user_id = data["username"]
        self.password = data["password"]
