
from django.views.generic import TemplateView
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy

from .models import Produto


class IndexView(ListView):
    model: Produto
    context_object_name = 'produtos'
    template_name = 'index.html'
    paginate_by = 4

    def get_queryset(self):
        return Produto.objects.all()


class CreateProdutoView(CreateView):
    model = Produto
    template_name = 'produto.html'
    fields = ['nome', 'preco', 'estoque', 'imagem']
    success_url = reverse_lazy('produto')


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
