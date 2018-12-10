import json

from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer

from battari.constant import TOKEN_HEADER
from battari.data.models.response.users import UsersSerializer
from battari.domain.user.users import Users
from battari.models import User


class UsersViewSet(viewsets.ViewSet):
    def retrieve(self, request, pk=None):
        user = self.get_queryset()  # me
        if user is None:
            return HttpResponse("Forbidden", status=403)

        data = user.objects.get(id=pk)  # detail user
        if data is None:
            return HttpResponse("Forbidden", status=403)

        users = Users(user, data)
        follows = users.follows()
        following = users.following()
        follower = users.follower()
        resp = [users.id, user.displayname, follows, user.icon,
                user.current_listening_track, user.comment, follower, following]
        resp_json = JSONRenderer().render(UsersSerializer(resp).data)

        serialized = UsersSerializer(data=resp_json)
        if not serialized.is_valid():
            return HttpResponse("Forbidden", status=403)
        return HttpResponse(resp_json, status=200, content_type='application/json')

    def get_queryset(self):
        if TOKEN_HEADER not in self.request.META:
            return None
        try:
            token = self.request.META[TOKEN_HEADER]
            user = User.objects.get(battari_token=token)
            return user
        except ObjectDoesNotExist:
            return None
