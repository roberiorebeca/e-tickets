from django.contrib import admin

from cadastros.models import Cliente, Categoria, Status


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome',)


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('descricao',)


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('descricao',)
