from django.contrib import admin
from AgendaApp.models import Contato, Cidade, Telefone, Interesse

# Register your models here.

class Telefones(admin.StackedInline):
    model = Telefone

class ContatoAdmin(admin.ModelAdmin):
    #colunas exibidas
    list_display = ['nome','email','cep','cidade','estado']
    # filtros
    list_filter =['data_nascimento','cidade','estado']
    # colunas com link para editar
    list_display_links = ['nome','email']
    search_fields = ['nome','apelido']
    inlines = [Telefones]
    filter_horizontal = ['Interesse']

admin.site.register(Contato, ContatoAdmin)
admin.site.register(Cidade)
admin.site.register(Telefone)
admin.site.register(Interesse)
    