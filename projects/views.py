from rest_framework import mixins, viewsets, permissions
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


class TagListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagModelSerializer
    permission_classes = (permissions.AllowAny,)
