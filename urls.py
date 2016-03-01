from rest_framework import routers
from views.rest import InsAdmEtpViewSet, InsAdmEtpInitialViewSet, IndividuViewSet

router = routers.SimpleRouter()
router.register(r'api/v1/InsAdmEtp', InsAdmEtpViewSet)
router.register(r'api/v1/InsAdmEtpInitial', InsAdmEtpInitialViewSet)
router.register(r'api/v1/Individu', IndividuViewSet)
# router.register(r'api/v1/DuckExamen', DuckExamenViewSet)

urlpatterns = router.urls