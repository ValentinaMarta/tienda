from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from WebTiendaShunApp.models import *


def index(request):
    #con esto le decimos a django donde tiene que buscar el html para mostrar el contenido de mi web
    return render(request, 'index.html')


def datosAlimentacion(request):
    producto= Alimentacion.objects.all()
    return render(request, 'alimentacion.html', {'producto': producto})

