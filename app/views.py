from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import car, rentacar


# página inicial
def home(request):
    return render(request, 'home.html')


# formulário de cadastro de clientes
def create(request):
    return render(request, 'cliente/create.html')


# inserção dos dados dos usuários no banco
def store(request):
    data = {}
    if request.POST['password'] != request.POST['password-conf']:
        data['msg'] = 'As senhas não coincidem.'
        data['class'] = 'alert-danger'
    else:
        user = User.objects.create_user(request.POST['user'], request.POST['email'], request.POST['password'])
        user.first_name = request.POST['name']
        user.last_name = request.POST['lastname']
        user.user_permissions.add(32)
        user.save()
        data['msg'] = 'Cadastro realizado!'
        data['class'] = 'alert-success'
    return render(request, 'cliente/create.html', data)


# formulário do painel de login
def painel(request):
    return render(request, 'cliente/painel.html')


# processar o login
def dologin(request):
    data = {}
    user = authenticate(username=request.POST['user'], password=request.POST['password'])
    if user is not None:
        login(request, user)
        return redirect('/dashboard/')
    else:
        data['msg'] = 'Usuário ou senha inválidos.'
        data['class'] = 'alert-danger'
        return render(request, 'cliente/painel.html', data)


# página inicial do dashboard
def dashboard(request):
    return render(request, 'dashboard/home.html')


# logout do sistema
def logouts(request):
    logout(request)
    return redirect('/cliente/painel')


def changePassword(request):
    data = {}
    user = User.objects.get(email=request.user.email)
    if request.POST['password'] != request.POST['password-conf']:
        data['msg'] = 'As senhas não coincidem.'
        data['class'] = 'alert-danger'
    else:
        user.set_password(request.POST['password'])
        user.save()
        data['msg'] = 'Você alterou sua senha com sucesso.'
        data['class'] = 'alert-success'
        logout(request)
        # return redirect('/painel/')
    return render(request, 'cliente/trocarSenha.html', data)


def trocarSenha(request):
    return render(request, 'cliente/trocarSenha.html')


# inserção dos dados dos carros no banco
def storeCar(request):
    # salvar novo carro no banco de dados
    data = {}
    novo_carro = car()
    novo_carro.placa = request.POST.get('placa')
    novo_carro.modelo = request.POST.get('modelo')
    novo_carro.marca = request.POST.get('marca')
    novo_carro.diaria = request.POST.get('diaria')
    novo_carro.save()
    data['msg'] = 'Carro adicionado!'
    data['class'] = 'alert-success'
    carros = {
        'carros': car.objects.all()
    }
    return render(request, 'carro/listar.html', carros)


# formulário de cadastro de carros
def addCar(request):
    return render(request, 'carro/addCar.html')


def carro(request):
    return render(request, 'carro/addCar.html')


def listar(request):
    carros = {
        'carros': car.objects.all()
    }
    return render(request, 'carro/listar.html', carros)


def cliente(request):
    return render(request, 'cliente/create.html')


def alugar(request, id):
    carro = car.objects.get(id=id)
    return render(request, 'carro/alugar.html')
    # return redirect('/listar')


def storeAlugar(request):
    novo_agendamento = rentacar()
    novo_agendamento.data_agendamento = request.POST.get('data_agendamento')
    novo_agendamento.dias_agendados = request.POST.get('dias_agendados')
    novo_agendamento.save()
    return render(request, 'carro/alugar.html')
    # return render(request, 'carro/alugar.html', {"carro":carro})