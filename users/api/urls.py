from django.conf.urls import url
from django.contrib import admin
from .views import (
    UserCreateAPIView,
    # UserLoginAPIView,
    FriendListCreateAPIView,
    FriendListDetailAPIView,
)


urlpatterns = [
    # users #
    # url(r'^login/$', UserLoginAPIView.as_view(), name='login'),
    url(r'^register/$', UserCreateAPIView.as_view(), name='register'),
    # FriendList #
    url(r'^friendlist/create/$', FriendListCreateAPIView.as_view(), name='friendlist_create'),
    url(r'^friendlist/(?P<pk>\d+)/$', FriendListDetailAPIView.as_view(), name='friendlist_detail'),
]
