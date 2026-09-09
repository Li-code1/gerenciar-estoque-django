from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .forms import AtualizarQuantidadeForm, ProdutoForm
from .models import Produto


class ProdutoListView(ListView):
    """Equivalente à opção 2 do CLI: lista os produtos em ordem alfabética."""

    model = Produto
    template_name = "estoque/produto_list.html"
    context_object_name = "produtos"
    # Produto.Meta.ordering já organiza por nome, mas deixamos explícito aqui também.
    queryset = Produto.objects.all().order_by("nome")


class ProdutoCreateView(SuccessMessageMixin, CreateView):
    """Equivalente à opção 1 do CLI: adicionar produto."""

    model = Produto
    form_class = ProdutoForm
    template_name = "estoque/produto_form.html"
    success_url = reverse_lazy("produto_list")
    success_message = "✅ Produto '%(nome)s' adicionado com sucesso!"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo"] = "Adicionar produto"
        return context


class ProdutoUpdateView(SuccessMessageMixin, UpdateView):
    """Equivalente à opção 4 do CLI: atualizar apenas a quantidade de um produto."""

    model = Produto
    form_class = AtualizarQuantidadeForm
    template_name = "estoque/produto_form.html"
    success_url = reverse_lazy("produto_list")
    success_message = "🔄 Quantidade de '%(nome)s' atualizada com sucesso!"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo"] = f"Atualizar quantidade de {self.object.nome}"
        return context


class ProdutoDeleteView(DeleteView):
    """Equivalente à opção 3 do CLI: remover produto (com confirmação)."""

    model = Produto
    template_name = "estoque/produto_confirm_delete.html"
    success_url = reverse_lazy("produto_list")

    def form_valid(self, form):
        nome = self.object.nome
        response = super().form_valid(form)
        messages.success(self.request, f"🗑️ Produto '{nome}' removido!")
        return response
