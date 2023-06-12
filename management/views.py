from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from management.models import ImagenesOferta, Oferta
from management.form import formOferta
from django.db.models import Q

# Create your views here.
@login_required(login_url='login')
def home(request):

    ofertas_recientes = Oferta.objects.filter(is_active=True, vendido=False)[:2]

    return render(request, 'home.html', {
        'ofertas_recientes': ofertas_recientes
    })

@login_required(login_url='login')
def busqueda(request, material=None):

    if material is not None:
        ofertas = Oferta.objects.filter(material=material, vendido=False, is_active=True)
        return render(request, 'busqueda.html', {
            'ofertas': ofertas
        })
    
    query = request.GET['buscar']
    ofertas = Oferta.objects.filter(Q(titulo__icontains=query) | Q(descripcion__icontains=query) | Q(material__icontains=query))

    return render(request, 'busqueda.html', {
        'ofertas': ofertas
    })

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
def offer_detail(request, pk_offer):

    offer = Oferta.objects.get(pk=pk_offer)
    estrellas = '&#9733; '
    calificacion_db = offer.usuario.calificacion
    calificacion = estrellas * calificacion_db

    return render(request, 'detalle_oferta.html', {
        'offer': offer,
        'calificacion': calificacion
    })

@login_required(login_url='login')
def published_offers(request, pk_usuario):

    ofertas = Oferta.objects.filter(usuario=pk_usuario, is_active=True, vendido=False)

    return render(request, 'articulos_en_oferta.html', {
        'ofertas': ofertas
    })

@login_required(login_url='login')
def sales_history(request):
    return render(request, 'historial_de_ventas.html')

@login_required(login_url='login')
def shopping_history(request):
    return render(request, 'historial_de_compras.html')