from django.core.exceptions import ObjectDoesNotExist
from django.db import models, transaction, IntegrityError
from django.db.models.signals import post_save
from django.dispatch import receiver

from base.models import Usuario


class Cliente(models.Model):
    """
    Modelo para guardar os dados do Cliente
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
def criar_usuario_do_cliente(sender, instance, created, **kwargs):
    post_save.disconnect(criar_usuario_do_cliente, sender=sender)
    if created:
        if instance.usuario is None:
            try:
                with transaction.atomic():
                    u = Usuario.objects.create_user(instance.nome, None, '123ABCD')
            except IntegrityError:
                u = Usuario.objects.get(username=instance.nome)

            instance.usuario = u
            instance.save()
    else:
        if instance.usuario is None:
            try:
                with transaction.atomic():
                    u = Usuario.objects.create_user(instance.nome, None, '123ABCD')
            except IntegrityError:
                u = Usuario.objects.get(username=instance.nome)

            instance.usuario = u
            instance.save()
        else:
            u = instance.usuario
            u.username = instance.nome
            u.save()

    post_save.connect(criar_usuario_do_cliente, sender=sender)


class Categoria(models.Model):
    """
    Modelo para guardar os dados do Categoria
    Ex: Dúvidas, Erros, Reclamações, Melhorias, Elogio, etc
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
    Ex: Pendente, Em Analise, etc
    """
    descricao = models.CharField(max_length=100,
                                 verbose_name='descrição'
                                 )

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name = 'status'
        verbose_name_plural = 'status'
