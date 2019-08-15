from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from .models import Empresa, Modulo, Usuario


class TestEmpresa(TestCase):
    """
    Teste do Modelo de Empresa
    """

    def test_add_empresa(self):
        emp = Empresa()

        emp.nome = 'Teste'
        emp.telefone = '0000000000'
        emp.endereco = 'Rual tal, S/N'
        emp.cidade = 'Sapezal MT'

        emp.save()

        self.assertEqual(str(emp), emp.nome, 'Verifica __str__ do objeto')
        self.assertEqual(emp.pk, 1, 'Verifica se salvou no banco')


class TestModulo(TestCase):
    """
    Teste do Modelo Modulo
    """

    def test_add_modulo(self):
        mod = Modulo()

        mod.descricao = 'Financeiro'

        mod.save()

        self.assertEqual(str(mod), mod.descricao, 'Verifica __str__ do objeto')
        self.assertEqual(mod.pk, 1, 'Verifica se salvou no banco')


class TesteModulo(TestCase):

    def setUp(self) -> None:
        """
        Class para testar a inclusão do cadastro de Módulo
        """
        self.user = Usuario.objects.create_superuser('admin', 'admin@admin.com.br', '123ABCD')
        self.api = APIClient()
        self.api.force_authenticate(user=self.user)
        self.url = '/base/'

    def test_add_modulo(self):
        url = f'{self.url}modulos/'
        post = dict(descricao='Teste')
        response = self.api.post(url, post, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
