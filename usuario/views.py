from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404, JsonResponse
# Create your views here.
from django.views.generic.detail import DetailView
from .models import Pessoa, Projeto
from .forms import ProjetoForm
from django.views.generic.edit import CreateView,UpdateView 
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.shortcuts import redirect

class HomeView(TemplateView):
    template_name = 'home.html'

class PessoaCreate(CreateView):
    model = Pessoa
    template_name = 'cliente_form.html'
    fields = ['nome','tipo','email','senha','cpf','data_nascimento','rua','numero','cep','bairro','cidade','numero_telefome','descricao']

    def get_success_url(self):
       return 'http://127.0.0.1:8000'


class PessoaListView(ListView):

    model = Pessoa
    template_name = 'cliente_list.html'
    paginate_by = 100  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = Pessoa.objects.all()
        return context

#class ProjetoCreate(CreateView):
#    model = Pessoa
#    template_name = 'cliente_form.html'
#    fields = ['nome','tipo','email','senha','cpf','data_nascimento','rua','numero','cep','bairro','cidade','numero_telefome','descricao']
#
#    def get_success_url(self):
#        return redirect('http://127.0.0.1:8000/projeto-listar')

class ProjetoCreate(CreateView):
    model = Projeto
    form_class = ProjetoForm
    template_name = 'projeto_form.html'
    
    def get_success_url(self):
        return 'http://127.0.0.1:8000/projeto-listar'

class ProjetoUpdate(UpdateView):
    model = Projeto
    fields = ['responsavel','colaborador','cliente','titulo','material','quantidade','valor','arquivo','status']
    template_name = 'projeto_form.html'
    def get_object(self, queryset=None):
        try:
            obj = Projeto.objects.get(pk=self.kwargs['pk'])
        except:
            raise Http404("Projeto não localizado")
        return obj

    def get_success_url(self):
        return 'http://127.0.0.1:8000/projeto-listar'

class ProjetoListView(ListView):

    model = Projeto
    template_name = 'projeto_list.html'
    paginate_by = 100  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = Projeto.objects.all()
        return context





class PessoaDetailView(DetailView):

    model = Pessoa
    template_name = 'cliente_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs.get(self.slug_url_kwarg)
        try:
            context['now'] = Pessoa.objects.get(pk=self.kwargs['pk'])
        except:
            raise Http404("Cliente não localizado")
        return context
        
        return context

