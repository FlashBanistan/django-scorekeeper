from django.conf.urls import url, include
# from .views import UserCreateAPIView
from rest_framework.routers import DefaultRouter
from .views import UserViewSet

user_router = DefaultRouter()
user_router.register(r'', UserViewSet)



urlpatterns = [
    url(r'^', include(user_router.urls), name='users'),
]

# urlpatterns = [
#     # users #
#     url(r'^register/$', UserCreateAPIView.as_view(), name='register'),
# ]
