import threading
from django.shortcuts import get_object_or_404
from rest_framework import mixins, viewsets, permissions, generics

from .serializers import (
    ProjectSerializer,
    TagModelSerializer,
    PhotoSerializer
)
from .models import Project, Tag, Photo
from .permissions import IsStaffOrReadOnly, IsStaff
from .helpers import capture_screenshot


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsStaffOrReadOnly,)

    def get_queryset(self):
        """
        Update queryset for `approved` and `sort` query params.
        """
        queryset = Project.objects.all()
        approved = self.request.query_params.get('approved', None)
        sort = self.request.query_params.get('sort', 'created-des')

        if approved is not None:
            if approved == 'true':
                queryset = queryset.filter(approved=True)
            elif approved == 'false':
                queryset = queryset.filter(approved=False)

        if sort == 'created-des':
            queryset = queryset.order_by('-created_at')
        elif sort == 'created-asc':
            queryset = queryset.order_by('created_at')

        return queryset

    def perform_create(self, serializer):
        project = serializer.save(creator=self.request.user)
        # Capture screenshot for Project
        thread = threading.Thread(target=capture_screenshot, args=(project,))
        thread.daemon = True
        thread.start()


class PhotoView(generics.UpdateAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    permission_classes = (IsStaff,)

    def get_object(self):
        project_id = self.kwargs.get('project_id', None)
        project = get_object_or_404(Project, id=project_id)

        self.check_object_permissions(self.request, project.photo)

        return project.photo


class TagListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Tag.objects.order_by('name')
    serializer_class = TagModelSerializer
    permission_classes = (permissions.AllowAny,)
