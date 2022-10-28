from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import ContatoForm
from .forms import ProdutoModelForm
from .models import Produto


def index(request):
    context = {
        'produtos': Produto.objects.all()
    }
    return render(request, 'index.html', context)

def contato(request):
    form = ContatoForm(request.POST or None)
    if str(request.method)=='POST':
        
        if form.is_valid():
            form.send_mail()
            messages.success(request, 'E-mail enviado com sucesso, logo entrarei em contato com vc :)')
            
            form = ContatoForm()
            
        else:      
            print(form.errors.as_data())    
            messages.error(request, 'E-mail não enviado')
            
              
    context = {'form': form}
    return render(request, 'contato.html', context)

def produto(request):
    if str(request.user) != 'AnonymousUser':
        if str(request.method) == 'POST':
            form = ProdutoModelForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, 'Produto salvo com sucesso')
                form = ProdutoModelForm()
            else:
                messages.error(request, 'Erro ao salvar produto')
        else:
            form = ProdutoModelForm()
        context = {'form': form}
                
        return render(request, 'produto.html', context)
    else:
        messages.error(request, 'voce não tem permissao')
        return redirect('index')
    
    

  #10 years later :( kkk