import json

from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer

from battari.data.models.request.register import RegisterSerializer
from battari.data.models.response.token import Token, TokenSerializer
from battari.domain.login.register import Register


class RegisterViewSet(viewsets.ViewSet):
    def create(self, request):
        body = json.loads(request.body.decode())
        serialized = RegisterSerializer(data=body)
        if not serialized.is_valid():
            return HttpResponse("Forbidden", status=403)
        data = serialized.validated_data
        # req = RegisterRequest(data.user_id, data.displayname, data.password)

        register = Register(data)
        if register.validate_user():
            register.create_user()
            token = register.create_token()
            resp = Token(token)
            token_json = JSONRenderer().render(TokenSerializer(resp).data)
            return HttpResponse(token_json, status=201, content_type='application/json')

        return HttpResponse("User Already Exists", status=409)
