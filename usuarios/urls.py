from django.urls import path, include

from .views import IndexView, EstoqueView, ProdutoView



urlpatterns = [
     path('', IndexView.as_view(), name='index'),
     path('contas/', include('django.contrib.auth.urls')),
    path('estoque', EstoqueView.as_view(), name='estoque'),
    path('produto', ProdutoView.as_view(), name='produto'),
]
     

