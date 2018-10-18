from rest_framework import routers
from .views import UserViewSet, LocationViewSet


router = routers.DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'locations', LocationViewSet)