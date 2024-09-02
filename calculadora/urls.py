from django.urls import path

#Vistas de la aplicacion "CALCULADORA
from . import views as vista_calculadora

urlpatterns = [
    path('', vista_calculadora.home),
    path('calculadora/', vista_calculadora.calculadora),
    path('armar_calculadora/', vista_calculadora.armar_calculadora),
    path('faq/', vista_calculadora.faq),
    path('contacto/', vista_calculadora.contacto),
    path('referrall/', vista_calculadora.referrall),
]