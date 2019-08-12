from django.contrib import admin

from movimentos.models import Chamado


@admin.register(Chamado)
class ChamadoAdmin(admin.ModelAdmin):
    list_display = ('data_abertura', 'cliente', 'usuario', 'status', 'data_fechamento')
    list_filter = ('status', 'data_abertura')
