from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from users.views import UserViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, base_name='user')

urlpatterns = [
    url(r'^', include(router.urls))
]
