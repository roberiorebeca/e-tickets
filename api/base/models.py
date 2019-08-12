from django.contrib.auth.models import AbstractUser
from django.db import models


class Empresa(models.Model):
    """
    Modelo para guardar dados da Empresa que vai usar o sistema
    """
    nome = models.CharField(max_length=150,
                            verbose_name='Razão Social'
                            )
    telefone = models.CharField(max_length=14
                                )
    endereco = models.CharField(max_length=100,
                                verbose_name='endereço'
                                )
    cidade = models.CharField(max_length=100,
                              verbose_name='cidade/uf'
                              )

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'empresa'
        verbose_name_plural = 'empresas'


class Modulo(models.Model):
    """
    Modelo para guardar os dados do módulo do sistema
    """
    descricao = models.CharField(max_length=100,
                                 verbose_name='descrição'
                                 )

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name = 'módulo'
        verbose_name_plural = 'módulos'


class Usuario(AbstractUser):
    """
    Modelo para vincular ao cadastro de Usuario do Django
    """
    cliente = models.BooleanField(default=False)
    suporte = models.BooleanField(default=False,
                                  verbose_name='suporte técnico'
                                  )
    desenvolvedor = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'usuário'
        verbose_name_plural = 'usuários'
