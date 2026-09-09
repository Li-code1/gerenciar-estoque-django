from django.urls import path

from . import views

urlpatterns = [
    path("", views.ProdutoListView.as_view(), name="produto_list"),
    path("produtos/novo/", views.ProdutoCreateView.as_view(), name="produto_create"),
    path("produtos/<int:pk>/atualizar/", views.ProdutoUpdateView.as_view(), name="produto_update"),
    path("produtos/<int:pk>/remover/", views.ProdutoDeleteView.as_view(), name="produto_delete"),
]
