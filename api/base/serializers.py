from django.contrib.auth.models import User
from rest_framework import serializers

from base.models import Empresa, Modulo, Usuario


class EmpresaSerializer(serializers.ModelSerializer):
    """
    Serializer para modelo de empresa
    """

    class Meta:
        model = Empresa
        fields = '__all__'


class ModuloSerializer(serializers.ModelSerializer):
    """
    Serializer para modelo dos Módulos
    """

    class Meta:
        model = Modulo
        fields = '__all__'


class UsuarioSerializer(serializers.ModelSerializer):
    """
    Serializer para modelo do Usuario
    """

    def create(self, validated_data):
        instance = super().create(validated_data)
        password = User.objects.make_random_password()
        instance.set_password(password)
        instance.save()
        return instance

    class Meta:
        model = Usuario
        exclude = ('password',)
