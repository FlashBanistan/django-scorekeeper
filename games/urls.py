from django.conf.urls import url, include
from . import views
from books_and_run import urls

app_name = 'games'

urlpatterns = [
    url(r'^', views.IndexView.as_view(), name='index'),
    url(r'^books_and_run/', include('books_and_run.urls')),
    # Add new game urls here.

]
