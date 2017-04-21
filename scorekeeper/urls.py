"""scorekeeper URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url, include
from django.contrib import admin
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

from books_and_run.api.urls import router
app_name = 'scorekeeper'

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/auth/get_token/', obtain_jwt_token),
    url(r'^api/auth/refresh_token/', refresh_jwt_token),
    url(r'^api/auth/verify_token/', verify_jwt_token),
    url(r'^api/users/', include("users.api.urls", namespace='users-api')),
    url(r'^api/books_and_run/', include(router.urls)),
]
