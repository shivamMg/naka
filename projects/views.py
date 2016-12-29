from rest_framework import mixins, viewsets, permissions
from .serializers import ProjectSerializer, TagModelSerializer
from .models import Project, Tag
from .permissions import IsStaffOrReadOnly


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsStaffOrReadOnly,)

    def get_queryset(self):
        """
        Update queryset for `approved` query param.
        """
        queryset = Project.objects.all()
        approved = self.request.query_params.get('approved', None)

        if approved is not None:
            if approved == 'true':
                queryset = queryset.filter(approved=True)
            elif approved == 'false':
                queryset = queryset.filter(approved=False)

        return queryset

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class TagListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagModelSerializer
    permission_classes = (permissions.AllowAny,)
