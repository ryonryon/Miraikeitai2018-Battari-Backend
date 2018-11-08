import json

from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.decorators import action

from battari.constant import TOKEN_HEADER
from battari.data.models.request.track_id import TrackSerializer
from battari.domain.me.me import Me
from battari.models import User
from battari.serializer import UserSerializer


class MeViewSet(viewsets.ViewSet):
    serializer_class = UserSerializer

    @action(detail=False, methods=['post'])
    def listening(self, request):
        user = self.get_queryset()
        me = Me(user)
        body = json.loads(request.body.decode())
        serialized = TrackSerializer(data=body)
        if not serialized.is_valid() or user is None:
            return HttpResponse("Forbidden", status=403)
        track_id = serialized.validated_data["track_id"]
        me.update_current_listenig_track(track_id)
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
