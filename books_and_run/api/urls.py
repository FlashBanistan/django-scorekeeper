from django.conf.urls import url
from django.contrib import admin
from .views import (
    # Statistic views
    StatisticsViewSet,
	)

from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'statistics', StatisticsViewSet)

urlpatterns = router.urls
