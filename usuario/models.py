from django.db import models
from django.urls import reverse
# Create your models here.
class Pessoa(models.Model):
    nome = models.CharField(name="nome",max_length=30)
    tipo =  models.CharField(name="tipo",max_length=30)
    email = models.EmailField() 
    senha = models.CharField(name="senha",max_length=30)
    cpf = models.IntegerField()
    data_nascimento = models.DateField()
    rua = models.CharField(name="rua",max_length=30)
    numero = models.IntegerField()
    cep = models.IntegerField()
    bairro =  models.CharField(name="bairro",max_length=30)
    cidade =  models.CharField(name="cidade",max_length=30)
    numero_telefome =  models.CharField(name="numero_telefome",max_length=30)
    descricao =  models.CharField(name="descricao",max_length=30)


    @property
    def get_detalhes_url(self):
        return reverse('detalhes-cliente', kwargs={'pk': self.pk})
        
    def __str__(self):
        return "{}".format(self.nome)



class Projeto(models.Model):
    responsavel = models.CharField(name="responsavel",max_length=30)
    colaborador = models.CharField(name="colaborador",max_length=30)
    cliente = models.CharField(name="cliente",max_length=30) 
    titulo = models.CharField(name="titulo",max_length=30)
    material = models.CharField(name="material",max_length=30)
    quantidade = models.IntegerField()
    valor = models.FloatField()
    arquivo = models.FileField(upload_to='projeto/', null=True,blank=True)
    status = models.BooleanField(name="status",default=False)

    @property
    def get_absolute_url(self):
        return reverse('update-projeto', kwargs={'pk': self.pk})
    