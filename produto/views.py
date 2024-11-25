from django.urls import reverse_lazy
from produto.forms import CategoriaForm, ProdutoForm
from produto.models import Categoria, Produto
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

class CategoriaListView(ListView, LoginRequiredMixin):
    model = Categoria
    template_name = 'categoria_list.html'

class CategoriaCreateView(CreateView, LoginRequiredMixin):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'categoria_form.html'
    success_url = reverse_lazy('categoria_list')

class CategoriaUpdateView(UpdateView, LoginRequiredMixin):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'categoria_form.html'
    success_url = reverse_lazy('categoria_list')

class CategoriaDeleteView(DeleteView, LoginRequiredMixin):
    model = Categoria
    template_name = 'categoria_confirm_delete.html'
    success_url = reverse_lazy('categoria_list')

####

class ProdutoListView(ListView, LoginRequiredMixin):
    model = Produto
    template_name = 'produto_list.html'

class ProdutoDetailView(DetailView, LoginRequiredMixin):
    model = Produto
    template_name = 'produto_detail.html'

class ProdutoCreateView(CreateView, LoginRequiredMixin):
    model = Produto
    form_class = ProdutoForm
    template_name = 'produto_form.html'
    success_url = reverse_lazy('produto_list')

class ProdutoUpdateView(UpdateView, LoginRequiredMixin):
    model = Produto
    form_class = ProdutoForm
    template_name = 'produto_form.html'
    success_url = reverse_lazy('produto_list')

class ProdutoDeleteView(DeleteView, LoginRequiredMixin):
    model = Produto
    template_name = 'produto_confirm_delete.html'
    success_url = reverse_lazy('produto_list')