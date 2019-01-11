from django.conf.urls import url
from django.contrib import admin
from .views import (
    # Statistic views
    StatisticsViewSet,
	)

from rest_framework.routers import DefaultRouter


statistics_router = DefaultRouter()
statistics_router.register(r'books_and_runs', StatisticsViewSet)

urlpatterns = statistics_router.urls
