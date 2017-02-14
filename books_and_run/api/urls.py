from django.conf.urls import url
from django.contrib import admin
from .views import (
    GameCreateAPIView,
    GameDeleteAPIView,
    GameUpdateAPIView,
    GameListAPIView,
    GameDetailAPIView
	)

urlpatterns = [
	url(r'^games/$', GameListAPIView.as_view(), name='list'),
    url(r'^games/create/$', GameCreateAPIView.as_view(), name='create'),
    url(r'^games/(?P<pk>\d+)/$', GameDetailAPIView.as_view(), name='detail'),
    url(r'^games/(?P<pk>[\w-]+)/edit/$', GameUpdateAPIView.as_view(), name='update'),
    url(r'^games/(?P<pk>[\w-]+)/delete/$', GameDeleteAPIView.as_view(), name='delete'),
]
