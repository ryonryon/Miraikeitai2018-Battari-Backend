import json

# from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer

from battari.constant import TOKEN_HEADER
from battari.data.models.response.users import UsersSerializer
from battari.domain.user.users import Users
from battari.models import User


class UserViewSet(viewsets.ViewSet):
    def retrieve(self, request, pk=None):
        user = self.get_queryset()
        if user is None:
            return HttpResponse("Forbidden", status=403)

        body = json.loads(request.body.decode())
        serialized = UserSerializer(data=body)
        if not serialized.is_valid():
            return HttpResponse("Forbidden", status=403)

        data = serialized.validated_data

        users = Users(data)
        id =
        displayname =
        follows =
        icon =
        current_listening_track =
        comment =
        follower = users.follower()
        following = users.following()

        resp = Users(user)
        resp_json = JSONRenderer().render(UsersSerializer(resp).data)
        return HttpResponse(resp_json, status=201, content_type='application/json')

    def get_queryset(self):
        if TOKEN_HEADER not in self.request.META:
            return None
        try:
            token = self.request.META[TOKEN_HEADER]
            user = User.objects.get(battari_token=token)
            return user
        except ObjectDoesNotExist:
            return None
