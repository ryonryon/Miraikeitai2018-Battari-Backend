import json

from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from rest_framework import viewsets

from battari.constant import TOKEN_HEADER
from battari.data.models.request.flick import FlickSerializer
from battari.domain.flick.flick import Flick
from battari.models import User


class FlickViewSet(viewsets.ViewSet):
    def create(self, request):
        user = self.get_queryset()
        if user is None:
            return HttpResponse("Forbidden", status=403)
        body = json.loads(request.body.decode())
        serialized = FlickSerializer(data=body)
        if not serialized.is_valid():
            return HttpResponse("Forbidden", status=403)
        data = serialized.validated_data
        flick = Flick(data, user)
        flick.firebase()
        return HttpResponse("OK", status=201)

    def get_queryset(self):
        if TOKEN_HEADER not in self.request.META:
            return None
        try:
            token = self.request.META[TOKEN_HEADER]
            user = User.objects.get(battari_token=token)
            return user
        except ObjectDoesNotExist:
            return None
