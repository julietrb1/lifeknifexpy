from rest_framework.decorators import api_view
from rest_framework.response import Response

from sec.serializers import AccountSerializer


@api_view(['GET'])
def account(request):
    if request.method == 'GET':
        serializer = AccountSerializer(request.user)
        return Response(serializer.data)
