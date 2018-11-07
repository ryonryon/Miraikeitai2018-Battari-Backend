import hashlib

from django.core.exceptions import ObjectDoesNotExist

from battari.domain.login.password import Password
from battari.models import User


class Register:
    def validate_user(self):
        try:
            User.objects.get(spotify_id=self.user_id)
            return False
        except ObjectDoesNotExist:
            return True

    def create_token(self):
        s = (self.password + ":" + self.user_id).encode()
        return hashlib.sha224(s).hexdigest()

    def create_user(self):
        salt = Password.create_salt()
        hashed_password = Password(self.password).hashing(salt)
        token = self.create_token()
        User(spotify_id=self.user_id,
             displayname=self.displayname,
             password=hashed_password,
             salt=salt.decode(),
             battari_token=token).save()

    def __init__(self, data):
        self.user_id = data["user_id"]
        self.displayname = data["displayname"]
        self.password = data["password"]
