from django.shortcuts import render
from ficheros.ficheiro_auxiliar import *



# Create your views here.


def aplicacao(request):
    return render(request, 'index.html')


def scaneo(request):
    lista_hosts = ESCANEO.lista_hosts()
    return render(request, 'index.html', {'lista': lista_hosts})


