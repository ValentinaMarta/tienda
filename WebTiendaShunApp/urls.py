from django.urls import path
from WebTiendaShunApp.views import *
from django.contrib import admin

urlpatterns = [
    path('', index, name='rutaPaginaPrincipal'),
    path('rutaDatosAlimentacion/', datosAlimentacion, name='enlaceAlimentacion'),
    path('rutaDatosMenaje/', datosAlimentacion, name='enlaceMenaje'),
    path('rutaDatosRopa/', datosAlimentacion, name='enlaceRopa'),
    path('rutaDatosJuguetes/', datosAlimentacion, name='enlaceJuguetes'),
]


