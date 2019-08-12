from rest_framework import serializers

from cadastros.models import Cliente, Categoria, Status


class ClienteSerializer(serializers.ModelSerializer):
    """
    Serializer para modelo de Cliente
    """

    class Meta:
        model = Cliente
        fields = '__all__'


class CategoriaSerializer(serializers.ModelSerializer):
    """
    Serializer para modelo de Categoria
    """

    class Meta:
        model = Categoria
        fields = '__all__'


class StatusSerializer(serializers.ModelSerializer):
    """
    Serializer para modelo de Status
    """

    class Meta:
        model = Status
        fields = '__all__'
