from django.urls import path

#Vistas de la aplicacion "CALCULADORA
from . import views as vista_calculadora

urlpatterns = [
    path('', vista_calculadora.home, name='home'),
    path('calculadora/', vista_calculadora.calculadora, name='calculadora'),
    path('faq/', vista_calculadora.faq, name='faq'),
    path('contacto/', vista_calculadora.contacto, name='contacto'),
    path('about/', vista_calculadora.about, name='about'),
]