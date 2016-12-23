from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet, get_tags

router = DefaultRouter()
router.register(r'projects', ProjectViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^tags/$', get_tags),
]
