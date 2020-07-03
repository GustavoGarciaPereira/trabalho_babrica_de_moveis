"""fabrica_de_moveis_gustavo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from . import  views
from .views import PessoaCreate,ProjetoCreate,HomeView,ProjetoListView,ProjetoUpdate,PessoaListView, PessoaDetailView
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('cliente', PessoaCreate.as_view(), name='index'),
    path('projeto', ProjetoCreate.as_view(), name='index'),
    path('projeto-listar', ProjetoListView.as_view(), name='index'),
    path('cliente-listar', PessoaListView.as_view(), name='index'),
    path('projeto-avaliar/<int:pk>/', ProjetoUpdate.as_view(), name='update-projeto'),
    path('cliente-detalhes/<int:pk>/', PessoaDetailView.as_view(), name='detalhes-cliente'),
]