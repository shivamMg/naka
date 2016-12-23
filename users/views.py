from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from .serializers import UserSerializer


@api_view(['POST'])
@permission_classes((AllowAny,))
def register(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            resp = {'username': serializer.data['username']}
            return Response(resp, status=HTTP_201_CREATED)
        else:
            return Response(serializer._errors, status=HTTP_400_BAD_REQUEST)
