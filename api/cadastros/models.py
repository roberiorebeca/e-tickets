from django.db import models


class Cliente(models.Model):
    """
    Modelo para guardar os dados do Cliente
    """
    nome = models.CharField(max_length=150)
    telefone = models.CharField(max_length=20)
    cidade = models.CharField(max_length=100,
                              verbose_name='cidade/uf'
                              )

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'cliente'
        verbose_name_plural = 'clientes'


class Categoria(models.Model):
    """
    Modelo para guardar os dados do Categoria
    """

    descricao = models.CharField(max_length=100,
                                 verbose_name='descrição'
                                 )

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'


class Status(models.Model):
    """
    Modelo para guardar os dados do Status
    """
    descricao = models.CharField(max_length=100,
                                 verbose_name='descrição'
                                 )

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name = 'status'
        verbose_name_plural = 'status'
