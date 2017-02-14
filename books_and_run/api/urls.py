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
    # Games #
	url(r'^games/$', GameListAPIView.as_view(), name='game_list'),
    url(r'^games/create/$', GameCreateAPIView.as_view(), name='game_create'),
    url(r'^games/(?P<pk>\d+)/$', GameDetailAPIView.as_view(), name='game_detail'),
    url(r'^games/(?P<pk>[\w-]+)/edit/$', GameUpdateAPIView.as_view(), name='game_update'),
    url(r'^games/(?P<pk>[\w-]+)/delete/$', GameDeleteAPIView.as_view(), name='game_delete'),
    # Scores #
    url(r'^scores/$', ScoreListAPIView.as_view(), name='score_list'),
    url(r'^scores/create/$', ScoreCreateAPIView.as_view(), name='score_create'),
    url(r'^scores/(?P<pk>\d+)/$', ScoreDetailAPIView.as_view(), name='score_detail'),
    url(r'^scores/(?P<pk>[\w-]+)/edit/$', ScoreUpdateAPIView.as_view(), name='score_update'),
    url(r'^scores/(?P<pk>[\w-]+)/delete/$', ScoreDeleteAPIView.as_view(), name='score_delete'),
]
