from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import *
from .forms import CursoForm, AvaliacaoForm


def home_view(request):
    avaliacoes = Avaliacao.objects.all()
    context = {
        'nome_empresa': 'EduDjango',
        'avaliacoes': avaliacoes
    }
    return render(request,'home.html', context)

def perfil_view(request):
    context = {
        'nome_funcionario': 'Gustavo',
        'cargo': 'Instrutor',
        'setor': 'TI',
    }
    return render(request,'perfil.html', context)

def status_view(request):
    context = {
        'id_servidor': '123.321',
        'status': 'ativo',
    }
    return render(request,'status.html', context)


def cursos_view(request):
    # 1. O usuário clicou no botão "Salvar" do Modal? (POST)
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save() # Salva no banco!
            # Redireciona para a mesma página para "limpar" o formulário 
            # e mostrar o novo curso na lista
            return redirect('cursos') 
            
    # 2. O usuário apenas acessou a página normalmente? (GET)
    else:
        form = CursoForm() # Cria um formulário vazio para ficar guardado no Modal

    # Se o usuário enviou o formulário do Modal (POST)
    if request.method == 'POST':
        form_avaliacao = AvaliacaoForm(request.POST)
        if form_avaliacao.is_valid():
            form_avaliacao.save()
            # Redireciona para recarregar a página e limpar o form
            return redirect('cursos') 
    else:
        # Se ele só acessou a página (GET), cria um form vazio
        form_avaliacao = AvaliacaoForm()

    # Busca todos os cursos para exibir na lista
    cursos = Curso.objects.all()

    #OPCIONAL, Só se quiser que apareça a lista de avaliações na tela
    # avaliacoes = Avaliacao.objects.all()
    
    context = {
        'cursos': cursos,
        #'avaliacao' : avaliacao, #OPCIONAL
        'form': form, # Manda o formulário pro HTML
        'form_avaliacao': form_avaliacao,
        'logado': request.user.is_authenticated,
        'usuario': request.user.username,
    }
    
    return render(request, 'cursos.html', context)

def login_view(request):
    if request.method == 'POST':
        # Passamos o request e os dados digitados
        form = AuthenticationForm(request, data=request.POST)
        
        # Se o usuário e senha estiverem corretos no banco
        if form.is_valid():
            user = form.get_user() # Resgata o usuário do banco
            login(request, user)   # Cria a sessão (Faz o login de fato)
            return redirect('home') # Manda para a página inicial
            
    else:
        form = AuthenticationForm()

    context = {
        'form': form
    }
    return render(request, 'login.html', context)

def cadastro_view(request):
    # FORMULÁRIO PADRÃO DE CADASTRO NO DJANGO
    form = UserCreationForm(request.POST)

    context = {
        'titulo_pagina': 'CADASTRO',
        'form': form
    }
    return render(request,'cadastro.html', context)