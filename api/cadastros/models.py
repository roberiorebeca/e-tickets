from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from base.models import Usuario


class Cliente(models.Model):
    """
    Modelo para guardar os dados do Cliente
    :TODO
        Não estou conseguindo atualizar usuario quando atualiza os dados do Cliente
    """
    empresa = models.ForeignKey(to='base.Empresa',
                                on_delete=models.DO_NOTHING,
                                null=True
                                )
    nome = models.CharField(max_length=150)
    telefone = models.CharField(max_length=20)
    cidade = models.CharField(max_length=100,
                              verbose_name='cidade/uf'
                              )
    usuario = models.ForeignKey(to='base.Usuario',
                                on_delete=models.DO_NOTHING,
                                null=True,
                                blank=True,
                                related_name='usuario_cliente')

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'cliente'
        verbose_name_plural = 'clientes'


@receiver(post_save, sender=Cliente)
def adicionar_cliente_adiciona_usuario(sender, instance, created, **kwargs):

    if created:
        if instance.usuario is None:
            usuario = Usuario.objects.create(username=instance.nome, password='123ABCD')
            post_save.disconnect(Cliente, sender=sender)
            instance.usuario = usuario
            post_save.connect(Cliente, sender=sender)
            instance.save()
    else:
        if instance.usuario is None:
            usuario = Usuario.objects.create(username=instance.nome, password='123ABCD')
            post_save.disconnect(Cliente, sender=sender)
            instance.usuario = usuario
            post_save.connect(Cliente, sender=sender)
            instance.save()
        else:
            post_save.disconnect(Cliente, sender=sender)
            instance.usuario_cliente.filter(username=instance.usuario).update(username=instance.nome)
            post_save.connect(Cliente, sender=sender)
            instance.save()




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
