import urllib.parse
import urllib.request


class Firebase:
    def flick_notify(self, flick):
        url = 'https://fcm.googleapis.com/fcm/send'
        headers = {'Authorization': self.authorization,
                   "Content-Type": "application/json"}
        method = "POST"
        req = urllib.request.Request(url=url, data=flick.encode("utf-8"), method=method, headers=headers)
        with urllib.request.urlopen(req) as res:
            return res.read().decode("utf-8")

    def __init__(self):
        self.authorization = "key=AAAAPNzE5vE:APA91bFSwqoCCzfJtTfSrvG7eG-HD_4NsUiALTXcUiA--mAXf2rIb3PF7lrtSYFJ0ZaLXBjitZAzL2tV1osmL961fs-yqSkW59bhKjz0eQvQZltyuhvgwMrSiANZXxzK4Ll6vvVzrOCS"
