# from django.conf.urls import url, include
# from rest_framework.routers import DefaultRouter
# from .views import UserViewSet
#
# user_router = DefaultRouter()
# user_router.register(r'', UserViewSet)
#
#
#
# urlpatterns = [
#     url(r'^', include(user_router.urls), name='users'),
# ]




"""
Everything under here is in testing:
"""
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from .views import CustomUserViewSet

user_router = DefaultRouter()
user_router.register(r'', CustomUserViewSet, base_name='user')

urlpatterns = [
    url(r'^', include(user_router.urls))
]
