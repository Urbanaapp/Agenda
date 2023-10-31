from django.contrib import admin
from AgendaApp.models import Contato

# Register your models here.
class ContatoAdmin(admin.ModelAdmin):
    #colunas exibidas
    list_display = ['nome','email','cep','cidade','estado']
    # filtros
    #  list_filter =['data_nascimento','cidade','estado']
    #colunas com link para editar
    list_display_links = ['nome','email']

admin.site.register(Contato, ContatoAdmin)

