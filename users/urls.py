from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet

user_router = DefaultRouter()
user_router.register(r'users', UserViewSet, base_name='user')

urlpatterns = [
    url(r'^', include(user_router.urls))
]
