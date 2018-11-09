class Firebase:
    def update_token(self, token):
        self.user.firebase_token = token
        self.user.save()

    def __init__(self, user):
        self.user = user
