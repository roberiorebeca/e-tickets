from rest_framework import viewsets

from base.models import Empresa, Modulo, Usuario
from base.serializers import EmpresaSerializer, ModuloSerializer, UsuarioSerializer


class EmpresaViewSet(viewsets.ModelViewSet):
    """
    Viewset para Modelo Empresa
    """
    serializer_class = EmpresaSerializer
    queryset = Empresa.objects.all()


class ModuloViewSet(viewsets.ModelViewSet):
    """
    Viewset para Modelo Modulo
    """
    serializer_class = ModuloSerializer
    queryset = Modulo.objects.all()


class UsuarioViewSet(viewsets.ModelViewSet):
    """
    Viewset para Modelo Usuario
    """
    serializer_class = UsuarioSerializer
    queryset = Usuario.objects.all()
