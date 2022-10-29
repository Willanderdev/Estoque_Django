
from django.views.generic import TemplateView

from .models import CustomUsuario as CS

from .models import Produto


class IndexView(TemplateView):
    template_name = 'index.html'
    
  

        # def get_context_data(self, **kwargs):
        #     context = super(IndexView, self).get_context_data(**kwargs)
        #     context['produtos'] = Produto.object.all()
        #     return context

class EstoqueView(TemplateView):
    template_name = 'Estoque.html'
    
    
class ProdutoView(TemplateView):
    template_name = 'produto.html'
       
