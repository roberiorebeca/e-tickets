from django.test import TestCase

from base.models import Empresa
from cadastros.models import Cliente, Categoria, Status


class TesteCliente(TestCase):
    """
    Teste do Cadastro de Cliente
    """

    def setUp(self):
        emp = Empresa()

        emp.nome = 'Teste'
        emp.telefone = '0000000000'
        emp.endereco = 'Rual tal, S/N'
        emp.cidade = 'Sapezal MT'

        emp.save()

    def test_add_cliente(self):
        c = Cliente()

        c.empresa = Empresa.objects.get()
        c.nome = 'Teste'
        c.telefone = '0000000000'
        c.cidade = 'Sapezal MT'
        # c.usuario = Usuario.objects.create_user(c.nome, None, '123ABC')

        c.save()

        self.assertEqual(str(c), c.nome, 'Verifica o __str__ do Modelo')
        self.assertEqual(c.pk, 1, 'Verifica se salvou no banco')

    def test_altera_cliente_altera_usuario(self):
        c = Cliente.objects.update(nome='Teste1')
        c.save()




class TesteCategoria(TestCase):
    """
    Teste para cadastro de Categoria
    """

    def test_add_categoria(self):
        cat = Categoria()

        cat.descricao = 'Teste'

        cat.save()

        self.assertEqual(str(cat), cat.descricao, 'Verifica o __str__ do Modelo')
        self.assertEqual(cat.pk, 1, 'Verifica se saçvou no banco')


class TesteStatus(TestCase):
    """
    Teste para cadastro de Status
    """

    def test_add_status(self):
        s = Status()

        s.descricao = 'Teste'

        s.save()

        self.assertEqual(str(s), s.descricao, 'Verifica o __str__ do Modelo')
        self.assertEqual(s.pk, 1, 'Verifica se saçvou no banco')
