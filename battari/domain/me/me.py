class Me:
    def update_current_listenig_track(self, track_id):
        self.user.current_listening_track = track_id
        self.user.save()

    def __init__(self, user):
        self.user = user
