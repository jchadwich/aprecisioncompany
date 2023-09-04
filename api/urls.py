from rest_framework.routers import DefaultRouter

from api.views import measurements


router = DefaultRouter()
router.register(
    "measurements", measurements.MeasurementViewSet, basename="measurements"
)


urlpatterns = router.urls
