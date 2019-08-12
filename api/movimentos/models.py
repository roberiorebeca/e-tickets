from django.db import models


class Chamado(models.Model):
    """
    Modelo para guardar os dados dos chamados
    """
    data_abertura = models.DateTimeField()
    cliente = models.ForeignKey(to='cadastros.Cliente',
                                on_delete=models.DO_NOTHING
                                )
    modulo = models.ForeignKey(to='base.Modulo',
                               on_delete=models.DO_NOTHING
                               )
    categoria = models.ForeignKey(to='cadastros.Categoria',
                                  on_delete=models.DO_NOTHING
                                  )
    status = models.ForeignKey(to='cadastros.Status',
                               on_delete=models.DO_NOTHING
                               )
    usuario = models.ForeignKey(to='base.Usuario',
                                on_delete=models.DO_NOTHING,
                                null=True,
                                blank=True)
    data_fechamento = models.DateTimeField()
    descricao = models.TextField(max_length=2000,
                                 verbose_name='descrição'
                                 )

    def __str__(self):
        return self.pk

    class Meta:
        verbose_name = 'chamado'
        verbose_name_plural = 'chamados'
