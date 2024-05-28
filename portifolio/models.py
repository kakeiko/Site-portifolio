from django.db import models
from datetime import datetime

OPCOES_CATEGORIA = [
    ("PYTHON", "Python"),
    ("JAVASCRIPT", "JavaScript"),
    ("DJANGO", "Django"),
    ("HTML", "HTML"),
    ("CSS", "CSS"),
]
OPCOES_STATUS = [
    ("Finalizado", "Finalizado"),
    ("Em andamento", "Em andamento"),
]

class Projeto(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    linguagem = models.CharField(max_length=100, choices=OPCOES_CATEGORIA, default='')
    foto = models.ImageField(upload_to="fotos/", blank=False)
    data_postagem = models.DateTimeField(default=datetime.now, blank=False)
    data_atualizacao = models.DateTimeField(default=datetime.now, blank=False)
    status = models.CharField(max_length=100, choices=OPCOES_STATUS, default='')
    video = models.FileField(upload_to="video/", blank=False, null=True)
    texto_objetivo = models.CharField(max_length=1000, blank=False,null=False)
    texto_projeto = models.CharField(max_length=1000, blank=False,null=False)
    link = models.CharField(max_length=100, blank=False, null= False)

    def __str__(self):
        return f"Projeto [nome={self.nome}]"


class CertificadoBD(models.Model):
    titulo = models.CharField(max_length=100, null=False, blank=False)
    foto = models.ImageField(upload_to="fotos/", blank=False)