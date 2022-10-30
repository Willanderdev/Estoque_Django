from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


from .views import IndexView, EstoqueView, CreateProdutoView, UpdateProdutoView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('contas/', include('django.contrib.auth.urls')),
    path('estoque', EstoqueView.as_view(), name='estoque'),
    path('produto', CreateProdutoView.as_view(), name='produto'),
    path('<int:pk>/update/', UpdateProdutoView.as_view(), name='upd_produto')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
