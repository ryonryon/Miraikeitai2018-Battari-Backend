import json

from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer

from battari.data.models.request.login import LoginSerializer
from battari.data.models.response.token import Token, TokenSerializer
from battari.domain.login.login import Login


class LoginViewSet(viewsets.ViewSet):
    def create(self, request):
        body = json.loads(request.body.decode())
        serialized = LoginSerializer(data=body)
        if not serialized.is_valid():
            return HttpResponse("Forbidden", status=403)

        data = serialized.validated_data

        login = Login(data)
        token = login.token()
        if token is None:
            return HttpResponse('Unauthorized', status=401)

        resp = Token(token)
        resp_json = JSONRenderer().render(TokenSerializer(resp).data)

        return HttpResponse(resp_json, status=201, content_type='application/json')
