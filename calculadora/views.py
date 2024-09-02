from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'index.html', name="home")

def calculadora(request):
    return render(request, 'calculadora.html', name="calculadora")

def armar_paquetes(request):
    return render(request, 'armar_paquetes.html', name="armar_paquetes")

def faq(request):
    return render(request, 'faq.html', name="faq")

def contacto(request):
    return render(request, 'contacto.html' , name="contacto")

def referrall(request):
    return render(request, 'referrall.html', name="referrall")