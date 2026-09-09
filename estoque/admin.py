from django.contrib import admin

from .models import Produto


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ("nome", "quantidade", "preco", "atualizado_em")
    search_fields = ("nome",)
    list_filter = ("atualizado_em",)
    ordering = ("nome",)
