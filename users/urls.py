from django.conf.urls import url, include
from rest_framework_jwt import views as api_auth

urlpatterns = [
    url(r'^', include('rest_framework.urls',
                      namespace='rest_framework')),
    url(r'^get-token/', api_auth.obtain_jwt_token),
    url(r'^refresh-token/', api_auth.refresh_jwt_token),
    url(r'^verify-token/', api_auth.verify_jwt_token),
]
