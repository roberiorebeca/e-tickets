from django.test import TestCase

from .models import Empresa, Modulo


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
