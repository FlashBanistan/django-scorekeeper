from django.conf.urls import url
from django.contrib import admin
from .views import (
    UserCreateAPIView,
    FriendListViewSet,
    # UserLoginAPIView,
    # FriendListCreateAPIView,
    # FriendListDetailAPIView,
)
from rest_framework.routers import DefaultRouter

friendlist_router = DefaultRouter()
friendlist_router.register(r'friendlist', FriendListViewSet)



urlpatterns = [
    # users #
    url(r'^register/$', UserCreateAPIView.as_view(), name='register'),
]

urlpatterns = urlpatterns + friendlist_router.urls
