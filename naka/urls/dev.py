from django.conf import settings
from django.conf.urls.static import static

from .common import *

urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)
