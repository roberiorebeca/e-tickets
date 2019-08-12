from rest_framework import routers

from base.views import EmpresaViewSet, ModuloViewSet, UsuarioViewSet

router = routers.DefaultRouter(trailing_slash=True)
router.register('empresas', EmpresaViewSet)
router.register('modulos', ModuloViewSet)
router.register('usuarios', UsuarioViewSet)

urlpatterns = router.urls
