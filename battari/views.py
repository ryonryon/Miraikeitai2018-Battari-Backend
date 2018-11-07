import json

from django.http import HttpResponseBadRequest, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets

from battari.domain.login.login import Login
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
