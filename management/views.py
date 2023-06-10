from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from management.models import ImagenesOferta, Oferta

# Create your views here.
@login_required(login_url='login')
def home(request):
    return render(request, 'home.html')

@login_required(login_url='login')
def busqueda(request):
    if request.method == 'GET':    
        return render(request, 'busqueda.html')

@login_required(login_url='login')
def publish_offer(request):

    if request.method == 'POST':
        titulo = request.POST['titulo']
        descripcion = request.POST['descripcion']
        cantidad = request.POST['cantKilos']
        valor = request.POST['valor']
        material = request.POST['material']
        imagenes = request.FILES['imagenes']
        usuario = request.user

        oferta = Oferta(titulo=titulo, descripcion=descripcion, cantidad=cantidad, valor=valor, material=material, usuario=usuario)
        oferta.save()

        for imagen in imagenes:
            
            img = ImagenesOferta.objects.create(imagen=imagen)
            oferta.imagenes.add(img)
        

    return render(request, 'publicar_oferta.html')

@login_required(login_url='login')
def offer_detail(request):
    return render(request, 'detalle_oferta.html')

@login_required(login_url='login')
def published_offers(request):
    return render(request, 'articulos_en_oferta.html')

@login_required(login_url='login')
def sales_history(request):
    return render(request, 'historial_de_ventas.html')

@login_required(login_url='login')
def shopping_history(request):
    return render(request, 'historial_de_compras.html')