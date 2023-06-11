from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from management.models import ImagenesOferta, Oferta
from management.form import formOferta

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

    form = formOferta()

    if request.method == 'POST':
        form = formOferta(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            form.instance.usuario = request.user
            oferta = form.save()
            imgs = [
                ImagenesOferta(imagen=image)
                for image in request.FILES.getlist('imagenes')
            ]
            ImagenesOferta.objects.bulk_create(imgs)
            oferta.imagenes.add(*imgs)
            return redirect('home')
        else:
            return form.errors
        
    return render(request, 'publicar_oferta.html', {
        'form': form
    })

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