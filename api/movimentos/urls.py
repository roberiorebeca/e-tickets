from rest_framework import routers

from movimentos.views import ChamadoViewSet

router = routers.DefaultRouter(trailing_slash=True)
router.register('chamados', ChamadoViewSet)

urlpatterns = router.urls
