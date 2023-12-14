"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import home, create, store, painel, dologin, dashboard, logouts, changePassword, trocarSenha, storeCar, \
    addCar, carro, listar, cliente, alugar, storeAlugar

urlpatterns = [
    # página inicial
    path('admin/', admin.site.urls),
    path('', home),
    # path('home/', home),
    # cliente
    path('cliente/create/', create),
    path('store/', store),
    path('cliente/painel/', painel),
    path('dologin/', dologin),
    path('cliente/trocarSenha/', trocarSenha),
    path('password/', changePassword),
    path('logouts/', logouts),
    path('cliente/', cliente),
    # carro
    path('carro/', carro),
    path('carro/addCar/', addCar),
    path('storeCar/', storeCar),
    path('carro/listar/', listar),
    path('carro/alugar/<int:id>', alugar, name='alugar'),
    path('storeAlugar/<int:id>', storeAlugar, name='storeAlugar'),

    path('dashboard/', dashboard),
]
