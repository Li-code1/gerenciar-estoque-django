from django import forms

from .models import Produto


class ProdutoForm(forms.ModelForm):
    """Formulário completo: usado para cadastrar um novo produto."""

    class Meta:
        model = Produto
        fields = ["nome", "quantidade", "preco"]
        widgets = {
            "nome": forms.TextInput(attrs={"class": "form-control", "placeholder": "Ex: Notebook"}),
            "quantidade": forms.NumberInput(attrs={"class": "form-control", "min": 0}),
            "preco": forms.NumberInput(attrs={"class": "form-control", "min": 0, "step": "0.01"}),
        }


class AtualizarQuantidadeForm(forms.ModelForm):
    """Formulário reduzido: reproduz a opção 4 do CLI (atualizar apenas a quantidade)."""

    class Meta:
        model = Produto
        fields = ["quantidade"]
        widgets = {
            "quantidade": forms.NumberInput(attrs={"class": "form-control", "min": 0, "autofocus": True}),
        }
