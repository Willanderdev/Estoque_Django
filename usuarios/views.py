
from django.views.generic import TemplateView
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import ProdutoModelForm
from django.urls import reverse_lazy

from .models import Produto


class IndexView(ListView):

    template_name = 'index.html'
    queryset = Produto.objects.all()
    context_object_name = 'produtos'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['produtos'] = Produto.objects.all()
        return context


class EstoqueView(TemplateView):
    template_name = 'Estoque.html'


class CreateProdutoView(CreateView):
    model = Produto
    template_name = 'produto.html'
    fields = ['nome', 'preco', 'estoque', 'imagem']
    success_url = reverse_lazy('index')


class UpdateProdutoView(UpdateView):
    template_name_suffix = "_update_form"
    
    model = Produto
    template_name = 'produto.html'
    
    fields = ['nome', 'preco', 'estoque', 'imagem']
    success_url = reverse_lazy('index')
