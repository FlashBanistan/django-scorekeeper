from rest_framework import routers
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import (
    # AllowAny,
    IsAuthenticated,
    # IsAdminUser,
    # IsAuthenticatedOrReadOnly,
)
from rest_framework.pagination import (
    LimitOffsetPagination,
    PageNumberPagination,
)
from rest_framework.filters import (
    SearchFilter,
    OrderingFilter,
)
from django_filters.rest_framework import DjangoFilterBackend



class DefaultsMixin(object):
    """Default settings for view authentication, permissions, filtering and pagination."""

    # authentication_classes = (
    #     JSONWebTokenAuthentication,
    # )
    #
    # permission_classes = (
    #     IsAuthenticated,
    # )

    paginate_by = 25
    paginate_by_param = 'page_size'
    max_paginate_by = 100
    filter_backends = (
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    )


class DefaultRouter(routers.DefaultRouter):
    """
    Extends `DefaultRouter` class to add a method for extending url routes from another router.
    """
    def extend(self, router):
        """
        Extend the routes with url routes of the passed in router.

        Args:
             router: SimpleRouter instance containing route definitions.
        """
        self.registry.extend(router.registry)