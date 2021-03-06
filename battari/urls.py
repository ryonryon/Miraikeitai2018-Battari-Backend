from rest_framework import routers

from battari.viewsets.firebase_view_set import FirebaseViewSet
from battari.viewsets.flick_view_set import FlickViewSet
from battari.viewsets.login_view_set import LoginViewSet
from battari.viewsets.me_view_set import MeViewSet
from battari.viewsets.register_view_set import RegisterViewSet

router = routers.SimpleRouter()
# router.register(r'users', UserViewSet)
router.register(r'auth', LoginViewSet, "auth")
router.register(r'register', RegisterViewSet, "register")
router.register(r'me', MeViewSet, "me")
router.register(r'firebase', FirebaseViewSet, "firebase")
router.register(r'flick', FlickViewSet, "flick")
