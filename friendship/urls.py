from rest_framework.routers import DefaultRouter
from friendship.views import FriendRequestViewSet, FriendViewSet


router = DefaultRouter()
router.register(r'friend_requests', FriendRequestViewSet)
router.register(r'friends', FriendViewSet)