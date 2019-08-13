from datetime import datetime, date

from django.test import TestCase
from django.utils import timezone

from base.models import Empresa, Usuario, Modulo
from cadastros.models import Cliente, Categoria, Status
from movimentos.models import Chamado


class TesteChamado(TestCase):
    """
    Teste de cadastro dos chamados
    """
    def setUp(self):
        emp = Empresa()

        emp.nome = 'Teste'
        emp.telefone = '0000000000'
        emp.endereco = 'Rual tal, S/N'
        emp.cidade = 'Sapezal MT'
        emp.save()

        c = Cliente()
        c.empresa = Empresa.objects.get()
        c.nome = 'Teste'
        c.telefone = '0000000000'
        c.cidade = 'Sapezal MT'
        c.save()

    def test_add_chamado(self):
        ch = Chamado()

        ch.data_abertura = timezone.now()
        ch.cliente = Cliente.objects.get()
        ch.modulo = Modulo.objects.create(descricao='Teste');
        ch.categoria = Categoria.objects.create(descricao='Teste')
        ch.status = Status.objects.create(descricao='Teste');
        ch.usuario = Usuario.objects.get(id=1)
        ch.data_fechamento = timezone.now()
        ch.assunto = 'Assunto'
        ch.descricao = 'Descrição'

        ch.save()

        self.assertEqual(str(ch), f'{ch.pk}', 'Verifica o __str__ do Modelo')
        self.assertEqual(ch.pk, 1, 'Verifica se salvou no banco')
