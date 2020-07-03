# posts/forms.py
from django import forms
from .models import Projeto, Pessoa

class ProjetoForm(forms.ModelForm):

    class Meta:
        model = Projeto
        fields = ['responsavel','colaborador','cliente','titulo','material','quantidade','valor','arquivo','status']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cliente'] = forms.ModelChoiceField(Pessoa.objects.all(),
                                                          empty_label="",
                                                          required=False)




class PessoaForm(forms.Form):
    senha = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Projeto
        
        field = ['nome','tipo','email','senha','cpf','data_nascimento','rua','numero','cep','bairro','cidade','numero_telefome','descricao']


