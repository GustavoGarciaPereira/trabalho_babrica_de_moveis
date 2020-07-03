from django.contrib import admin

# Register your models here.

from .models import Projeto, Pessoa

class ProjetoAdmin(admin.ModelAdmin):
    pass
admin.site.register(Projeto, ProjetoAdmin)


class PessoaAdmin(admin.ModelAdmin):
    pass
admin.site.register(Pessoa, PessoaAdmin)
