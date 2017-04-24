from django.conf.urls import url
from .views import UserCreateAPIView

from rest_framework.routers import DefaultRouter



urlpatterns = [
    # users #
    url(r'^register/$', UserCreateAPIView.as_view(), name='register'),
]
