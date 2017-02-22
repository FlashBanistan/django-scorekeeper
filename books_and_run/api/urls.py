from django.conf.urls import url
from django.contrib import admin
from .views import (
    # Game views
    GameCreateAPIView,
    GameDeleteAPIView,
    GameUpdateAPIView,
    GameListAPIView,
    GameDetailAPIView,
    # Score views
    ScoreCreateAPIView,
    ScoreDeleteAPIView,
    ScoreUpdateAPIView,
    ScoreListAPIView,
    ScoreDetailAPIView,
    # Statistic views
    StatisticsCreateAPIView,
    StatisticsDeleteAPIView,
    StatisticsUpdateAPIView,
    StatisticsListAPIView,
    StatisticsDetailAPIView,
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
    # Statistics #
    url(r'^statistics/$', StatisticsListAPIView.as_view(), name='statistics_list'),
    url(r'^statistics/create/$', StatisticsCreateAPIView.as_view(), name='statistics_create'),
    url(r'^statistics/(?P<pk>\d+)/$', StatisticsDetailAPIView.as_view(), name='statistics_detail'),
    url(r'^statistics/(?P<pk>[\w-]+)/edit/$', StatisticsUpdateAPIView.as_view(), name='statistics_update'),
    url(r'^statistics/(?P<pk>[\w-]+)/delete/$', StatisticsDeleteAPIView.as_view(), name='statistics_delete'),

]
