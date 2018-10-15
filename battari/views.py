from django.shortcuts import render

from rest_framework import viewsets
from battari.serializer import UserSerializer, LocationSerializer
from .models import User, Location


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
