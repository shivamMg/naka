from rest_framework import viewsets, permissions
from .serializers import ProjectSerializer
from .models import Project
from .permissions import IsStaffOrReadOnly


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsStaffOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)
