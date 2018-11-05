from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json

from rest_framework import viewsets
from rest_framework.views import APIView

from battari.serializer import UserSerializer, LocationSerializer
from .models import User, Location

from django.http import HttpRequest, HttpResponse


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


@csrf_exempt
# def firebase(request):
#     if request.method == "POST":
#         print(json.loads(request.body))
#         print(request.content_params.values())
#         post_token = request.content_params.values()
#         t = User.objects.get(token=post_token)
#         t.token
#     return HttpResponse(request.content_params)

def firebase(request):
    if request.method == "POST":
        posted_token = request.META["HTTP_X_TOKEN"]
        posted_firabase_token = json.loads(request.body)["token"]
        # count_account = User.objects.only('id').count()
        obj, created = User.objects.update_or_create(
            displayname=posted_token,
            defaults={'firebase_token': posted_firabase_token
                      }
        )
    return HttpResponse(request)
