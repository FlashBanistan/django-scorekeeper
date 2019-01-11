from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from .views import FriendListViewSet



friendlist_router = DefaultRouter()
friendlist_router.register(r'friends', FriendListViewSet)

urlpatterns = [
    url(r'^', include(friendlist_router.urls), name='friends'),
]
