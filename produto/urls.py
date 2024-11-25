from django.urls import path
from produto.views import CategoriaDeleteView, CategoriaListView, CategoriaCreateView, CategoriaUpdateView, ProdutoCreateView, ProdutoDeleteView, ProdutoListView, ProdutoUpdateView, ProdutoDetailView


urlpatterns = [
    path("categoria/", CategoriaListView.as_view(), name="categoria_list"),
    path("categoria/criar", CategoriaCreateView.as_view(), name="categoria_form"),
    path("categoria/<int:pk>/editar", CategoriaUpdateView.as_view(), name="categoria_update"),
    path("categoria/<int:pk>/excluir", CategoriaDeleteView.as_view(), name="categoria_delete"),
    #######
    path("produto/", ProdutoListView.as_view(), name="produto_list"),
    path("produto/<int:pk>/detalhe/", ProdutoDetailView.as_view(), name="produto_detail"),
    path("produto/criar/", ProdutoCreateView.as_view(), name="produto_form"),
    path("produto/produto/<int:pk>/editar", ProdutoUpdateView.as_view(), name="produto_update"),
    path("produto/produto/<int:pk>/excluir", ProdutoDeleteView.as_view(), name="produto_delete"),
]