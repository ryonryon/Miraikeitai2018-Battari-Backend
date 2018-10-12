from rest_framework import routers
from .views import UserViewSet, LocationViewSet


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'locations', LocationViewSet)