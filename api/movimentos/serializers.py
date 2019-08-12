from rest_framework import serializers

from movimentos.models import Chamado


class ChamadoSerializer(serializers.ModelSerializer):
    """
    Serializer para modelo de Chamado
    """

    class Meta:
        model = Chamado
        fields = '__all__'
