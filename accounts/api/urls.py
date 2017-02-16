from django.conf.urls import url
from django.contrib import admin
from .views import (
    UserCreateAPIView,
    UserLoginAPIView,
)


urlpatterns = [
    # Accounts #
    url(r'^login/$', UserLoginAPIView.as_view(), name='login'),
    url(r'^register/$', UserCreateAPIView.as_view(), name='register'),
]
