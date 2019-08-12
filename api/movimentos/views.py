from rest_framework import viewsets

from movimentos.models import Chamado
from movimentos.serializers import ChamadoSerializer


class ChamadoViewSet(viewsets.ModelViewSet):
    """
    ViewSet para Modelo Chamado
    """

    serializer_class = ChamadoSerializer
    queryset = Chamado.objects.all()
