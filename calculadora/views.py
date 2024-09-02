from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'index.html')

def calculadora(request):
    return render(request, 'calculadora.html', name="calculadora")

def faq(request):
    return render(request, 'faq.html', name="faq")

def contacto(request):
    return render(request, 'contacto.html' , name="contacto")

def about(request):
    return render(request, 'about.html', name="about")