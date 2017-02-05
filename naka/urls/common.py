from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from projects.views import (
    ProjectViewSet,
    TagListViewSet,
    PhotoView
)
from users.views import UserCreateViewSet

router = DefaultRouter()
router.register(r'projects', ProjectViewSet)
router.register(r'tags', TagListViewSet)
router.register(r'users', UserCreateViewSet)

urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^api/projects/(?P<project_id>[0-9]+)/photo/$', PhotoView.as_view()),
    url(r'^auth/', include('naka.urls.auth')),
]
