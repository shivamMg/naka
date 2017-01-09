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
        serializer.save(creator=self.request.user)


class TagListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Tag.objects.order_by('name')
    serializer_class = TagModelSerializer
    permission_classes = (permissions.AllowAny,)
