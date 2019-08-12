from rest_framework import viewsets

from cadastros.models import Cliente, Categoria, Status
from cadastros.serializers import ClienteSerializer, CategoriaSerializer, StatusSerializer


class ClienteViewSet(viewsets.ModelViewSet):
    """
    ViewSet para Modelo Cliente
    """

    serializer_class = ClienteSerializer
    queryset = Cliente.objects.all()


class CategoriaViewSet(viewsets.ModelViewSet):
    """
    ViewSet para Modelo Categoria
    """

    serializer_class = CategoriaSerializer
    queryset = Categoria.objects.all()


class StatusViewSet(viewsets.ModelViewSet):
    """
    ViewSet para Modelo Status
    """

    serializer_class = StatusSerializer
    queryset = Status.objects.all()
