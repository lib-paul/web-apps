from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CalculadoraForm
# Create your views here.


#NAVEGACIÓN
def home(request):
    url_actual = request.get_full_path()
    print(url_actual)
    return render(request, 'index.html')

def calculadora(request):
    
    if request.method == 'POST':
        form = CalculadoraForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('success')
    else:
        form = CalculadoraForm()
    url_actual = request.get_full_path()
    print(url_actual)
    return render(request, 'calculadora.html', {'form': form})

def faq(request):
    return render(request, 'faq.html')

def contacto(request):
    return render(request, 'contacto.html')

def about(request):
    return render(request, 'about.html')
