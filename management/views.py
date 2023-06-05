from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    return render(request, 'home.html')

def busqueda(request):
    if request.method == 'GET':    
        return render(request, 'busqueda.html')