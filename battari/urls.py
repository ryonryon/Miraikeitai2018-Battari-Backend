from rest_framework import routers

from battari.viewsets.login_view_set import LoginViewSet
from battari.viewsets.register_view_set import RegisterViewSet
from .views import UserViewSet

router = routers.SimpleRouter()
router.register(r'users', UserViewSet)
router.register(r'auth', LoginViewSet, "auth")
router.register(r'register', RegisterViewSet, "register")
