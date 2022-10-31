
from django.views.generic import TemplateView
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy

from .models import Produto


class IndexView(ListView):
    model: Produto
    paginate_by: 3
    queryset = Produto.objects.all()
    context_object_name = 'produtos'
    template_name = 'index.html'
    
    ordering = 'id'

    # def get_context_data(self, **kwargs):
    #     context = super(IndexView, self).get_context_data(**kwargs)
    #     context['produtos'] = Produto.objects.all()
    #     return context


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


class DeleteProdutoView(DeleteView):
    template_name_suffix = "_confirm_delete"
    model = Produto
    template_name = 'produto_del.html'
    success_url = reverse_lazy('index')
