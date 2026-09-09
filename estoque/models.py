from django.core.validators import MinValueValidator
from django.db import models


class Produto(models.Model):
    """Representa um item do estoque (equivalente ao dicionário aninhado da versão CLI)."""

    nome = models.CharField(
        max_length=150,
        unique=True,
        verbose_name="Nome",
        help_text="Nome do produto (deve ser único).",
    )
    quantidade = models.PositiveIntegerField(
        default=0,
        validators=[MinValueValidator(0)],
        verbose_name="Quantidade",
    )
    preco = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        verbose_name="Preço",
    )
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["nome"]
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"

    def __str__(self):
        return f"{self.nome} (Qtd: {self.quantidade} | R$ {self.preco})"
