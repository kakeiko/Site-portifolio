from django.contrib import admin
from portifolio.models import Projeto, CertificadoBD


class ListandoCertificados(admin.ModelAdmin):
    list_display = ("id", "titulo")
    list_display_links = ("id", "titulo")
    search_fields = ("titulo",)
    list_per_page = 10

class ListandoProjetos(admin.ModelAdmin):
    list_display = ("id", "nome", "linguagem")
    list_display_links = ("id", "nome")
    search_fields = ("nome",)
    list_filter = ("linguagem",)
    list_per_page = 10

admin.site.register(Projeto, ListandoProjetos)
admin.site.register(CertificadoBD, ListandoCertificados)

