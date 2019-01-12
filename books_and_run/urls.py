from rest_framework.routers import DefaultRouter
from books_and_run.views import StatisticsViewSet


router = DefaultRouter()
router.register(r'books_and_runs', StatisticsViewSet)

urlpatterns = router.urls
