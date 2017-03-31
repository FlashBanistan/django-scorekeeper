from django.conf.urls import url
from django.contrib import admin
from .views import (
    # Statistic views
    StatisticsCreateAPIView,
    StatisticsDeleteAPIView,
    StatisticsUpdateAPIView,
    StatisticsListAPIView,
    StatisticsDetailAPIView,
	)

urlpatterns = [
    # Statistics #
    url(r'^statistics/$', StatisticsListAPIView.as_view(), name='statistics_list'),
    url(r'^statistics/create/$', StatisticsCreateAPIView.as_view(), name='statistics_create'),
    url(r'^statistics/(?P<pk>\d+)/$', StatisticsDetailAPIView.as_view(), name='statistics_detail'),
    url(r'^statistics/(?P<pk>[\w-]+)/edit/$', StatisticsUpdateAPIView.as_view(), name='statistics_update'),
    url(r'^statistics/(?P<pk>[\w-]+)/delete/$', StatisticsDeleteAPIView.as_view(), name='statistics_delete'),

]
