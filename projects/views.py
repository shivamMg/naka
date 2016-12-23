from rest_framework import viewsets, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from .serializers import ProjectSerializer, TagModelSerializer
from .models import Project, Tag
from .permissions import IsStaffOrReadOnly


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsStaffOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def get_tags(request):
    if request.method == 'GET':
        serializer = TagModelSerializer(Tag.objects.all(), many=True)
        return Response(serializer.data, status=HTTP_200_OK)
