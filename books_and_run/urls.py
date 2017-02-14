from django.conf.urls import url, include
from . import views

app_name = 'books_and_run'

urlpatterns = [
    url(r'^', views.IndexView.as_view(), name='index'),

]
