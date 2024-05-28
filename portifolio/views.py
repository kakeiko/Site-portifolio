from django.shortcuts import render, get_object_or_404
from portifolio.models import Projeto, CertificadoBD

def index(request):
    return render(request, 'html/index.html')

def port(request):
    pro = Projeto.objects.order_by("data_postagem").all()
    return render(request, 'html/portifolio.html', {"cards": pro})

def educacao(request):
    return render(request, 'html/educacao.html')

def sobre(request):
    return render(request, 'html/sobre-mim.html')

def projeto(request, pro_id):
    projetos = get_object_or_404(Projeto, pk=pro_id)
    return render(request, 'html/projeto.html',{"projeto": projetos} )

def buscar(request):
    pro = Projeto.objects.order_by("data_postagem").all()

    if "buscar" in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            pro = pro.filter(nome__icontains=nome_a_buscar)
    
    return render(request, 'html/buscar.html', {"cards": pro})

def certificado(request):
    certf = CertificadoBD.objects.all()
    return render(request, 'html/certificado.html', {"cards": certf})
