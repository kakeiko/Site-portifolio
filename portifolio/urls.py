from django.urls import path
from portifolio.views import index, port, educacao, sobre, projeto,certificado,buscar

urlpatterns = [
    path('', index, name='home'),
    path('portifolio/', port, name='port'),
    path('educacao/', educacao, name='edu'),
    path('sobre-mim/', sobre, name='sobre'),
    path('projeto/<int:pro_id>', projeto, name='projeto'),
    path('certificado/', certificado, name='cert'),
    path('buscar', buscar, name='buscar'),

]