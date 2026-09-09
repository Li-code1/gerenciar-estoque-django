from django import forms

from .models import Produto


class PrecoWidget(forms.NumberInput):
    """NumberInput que aceita vírgula como separador decimal (padrão brasileiro)."""

    def value_from_datadict(self, data, files, name):
        valor = super().value_from_datadict(data, files, name)
        if valor:
            valor = str(valor).replace(",", ".")
        return valor


class ProdutoForm(forms.ModelForm):
    """Formulário completo: usado para cadastrar um novo produto."""

    class Meta:
        model = Produto
        fields = ["nome", "quantidade", "preco"]
        widgets = {
            "nome": forms.TextInput(attrs={"class": "form-control", "placeholder": "Ex: Notebook"}),
            "quantidade": forms.NumberInput(attrs={"class": "form-control", "min": 0}),
            "preco": PrecoWidget(attrs={"class": "form-control", "min": 0, "step": "0.01", "placeholder": "Ex: 4500 ou 4500,00"}),
        }


class AtualizarQuantidadeForm(forms.ModelForm):
    """Formulário reduzido: reproduz a opção 4 do CLI (atualizar apenas a quantidade)."""

    class Meta:
        model = Produto
        fields = ["quantidade"]
        widgets = {
            "quantidade": forms.NumberInput(attrs={"class": "form-control", "min": 0, "autofocus": True}),
        }
