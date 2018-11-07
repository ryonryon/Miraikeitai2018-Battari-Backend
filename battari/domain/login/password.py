import bcrypt


class Password:
    def hashing(self, salt):
        hashed_password = bcrypt.hashpw(self.input_password, salt)
        return hashed_password

    @staticmethod
    def create_salt():
        salt = bcrypt.gensalt(rounds=10, prefix=b'2a')
        return salt

    def __init__(self, password):
        self.input_password = password
