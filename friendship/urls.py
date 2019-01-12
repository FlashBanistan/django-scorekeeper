from rest_framework.routers import DefaultRouter
from friendship.views import FriendshipRequestViewSet


router = DefaultRouter()
router.register(r'friend_requests', FriendshipRequestViewSet)

urlpatterns = router.urls
