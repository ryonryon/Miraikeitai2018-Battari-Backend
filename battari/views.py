import json

from django.http import HttpResponseBadRequest, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets

from battari.domain.login.login import Login
from battari.domain.login.register import Register
from battari.serializer import UserSerializer, LocationSerializer
from .models import User, Location


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


@csrf_exempt
def login_controller(request):
    if request.method != "POST":
        return HttpResponseBadRequest

    body = json.loads(request.body.decode())

    login = Login(body)
    token = login.token()
    if token is None:
        return HttpResponse('Unauthorized', status=401)

    return HttpResponse("OK")


@csrf_exempt
def register_controller(request):
    if request.method != "POST":
        return HttpResponseBadRequest

    body = json.loads(request.body.decode())

    register = Register(body)
    if register.validate_user():
        register.create_user()
        return HttpResponse("OK", status=201)

    return HttpResponse("User Already Exists", status=409)
