from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    return render(request, 'home.html')

def busqueda(request):
    if request.method == 'GET':    
        return render(request, 'busqueda.html')
    
def publish_offer(request):
    return render(request, 'publicar_oferta.html')

def offer_detail(request):
    return render(request, 'detalle_oferta.html')