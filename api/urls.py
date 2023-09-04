from rest_framework.routers import DefaultRouter

from api.views import measurements, tables


router = DefaultRouter()
router.register(
    "measurements", measurements.MeasurementViewSet, basename="measurements"
)
router.register(
    "tables/customers", tables.CustomerTableViewSet, basename="tables-customers"
)


urlpatterns = router.urls
