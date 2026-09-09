from decimal import Decimal

from django.test import TestCase
from django.urls import reverse

from .models import Produto


class ProdutoModelTests(TestCase):
    def test_str_mostra_nome_quantidade_e_preco(self):
        produto = Produto.objects.create(nome="Mouse", quantidade=20, preco=Decimal("150.00"))
        self.assertIn("Mouse", str(produto))

    def test_nome_e_unico(self):
        Produto.objects.create(nome="Notebook", quantidade=5, preco=Decimal("3500.00"))
        with self.assertRaises(Exception):
            Produto.objects.create(nome="Notebook", quantidade=1, preco=Decimal("1.00"))


class ProdutoViewsTests(TestCase):
    def setUp(self):
        self.produto = Produto.objects.create(nome="Teclado", quantidade=10, preco=Decimal("200.00"))

    def test_listagem_mostra_produto_cadastrado(self):
        response = self.client.get(reverse("produto_list"))
        self.assertContains(response, "Teclado")

    def test_criar_produto(self):
        response = self.client.post(
            reverse("produto_create"),
            {"nome": "Monitor", "quantidade": 3, "preco": "899.90"},
        )
        self.assertRedirects(response, reverse("produto_list"))
        self.assertTrue(Produto.objects.filter(nome="Monitor").exists())

    def test_atualizar_quantidade(self):
        response = self.client.post(
            reverse("produto_update", args=[self.produto.pk]),
            {"quantidade": 99},
        )
        self.assertRedirects(response, reverse("produto_list"))
        self.produto.refresh_from_db()
        self.assertEqual(self.produto.quantidade, 99)

    def test_remover_produto(self):
        response = self.client.post(reverse("produto_delete", args=[self.produto.pk]))
        self.assertRedirects(response, reverse("produto_list"))
        self.assertFalse(Produto.objects.filter(pk=self.produto.pk).exists())
