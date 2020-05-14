from django.contrib.auth import login
from rest_framework.authentication import BasicAuthentication
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from sec.serializers import AccountSerializer


@api_view(['GET'])
def account(request):
    if request.method == 'GET':
        serializer = AccountSerializer(request.user)
        return Response(serializer.data)


class MyBasicAuthentication(BasicAuthentication):
    def authenticate(self, request):
        result = super().authenticate(request)
        if not (result and result[0]):
            return None
        request._user = result[0]
        login(request, result[0])
        return result


class CustomLoginView(APIView):
    authentication_classes = (MyBasicAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        serializer = AccountSerializer(request.user)
        return Response(serializer.data)
