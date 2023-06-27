from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, HttpResponse
from management.models import *
from management.forms import formOferta, formMensaje
from django.db.models import Q
from django.contrib import messages

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
            messages.error(request, form.errors)
            return render(request, 'publicar_oferta.html', {
                'form': form
            })
        
    return render(request, 'publicar_oferta.html', {
        'form': form
    })

@login_required(login_url='login')
def offer_detail(request, pk_offer):

    offer = Oferta.objects.get(pk=pk_offer)
    estrellas = '&#9733; '
    calificacion_db = offer.usuario.calificacion
    calificacion = estrellas * calificacion_db

    # Form de mensajes
    form_mensaje = formMensaje()

    if request.method == 'POST':
        form = formMensaje(request.POST)
        if form.is_valid():
            form.instance.emisor = request.user
            form.instance.receptor = offer.usuario
            form.instance.oferta = offer
            form.save()
            messages.success(request, 'Tu mensaje ha sido enviado con éxito.')
            return redirect('offer_detail', pk_offer=offer.id)
        else:
            return HttpResponse(form.errors)

    return render(request, 'detalle_oferta.html', {
        'offer': offer,
        'calificacion': calificacion,
        'formMensaje': form_mensaje
    })

@login_required(login_url='login')
def published_offers(request, pk_usuario):

    ofertas = Oferta.objects.filter(usuario=pk_usuario, is_active=True, vendido=False)

    return render(request, 'articulos_en_oferta.html', {
        'ofertas': ofertas
    })

@login_required(login_url='login')
def saled_offer(request, pk_offer):

    oferta = Oferta.objects.get(id=pk_offer)
    oferta.vendido = True
    oferta.save()

    return redirect('published_offers', pk_usuario=request.user.id)

@login_required(login_url='login')
def buy_offer(request, pk_offer):

    try:

        # 1. Se busca primero la oferta que se vendió y se marca como vendido
        oferta = Oferta.objects.get(id=pk_offer)
        oferta.vendido = True
        oferta.save()


        # Se crea una nueva venta
        venta = Venta(oferta=oferta)
        venta.save()
        

        # Se registra la compra
        compra = Compra(venta=venta, comprador=request.user)
        compra.save()
        print(compra)

        # Se notifica al usuario que está publicando la oferta
        Notificacion.objects.create(oferta=oferta, mensaje=f'{NOTIFICACIONES_CHOICES[1][0]} - {oferta.titulo}', receptor=oferta.usuario)

        print('todo ok')
        # Se redirecciona
        return redirect('articulo_comprado')
    except Exception as e:
        print(e)
        return e

@login_required(login_url='login')
def sales_history(request):

    ventas_usuario = Venta.objects.filter(oferta__usuario=request.user)

    return render(request, 'historial_de_ventas.html', {
        'ventas_usuario': ventas_usuario
    })

@login_required(login_url='login')
def shopping_history(request):

    compras_usuario = Compra.objects.filter(comprador=request.user)

    return render(request, 'historial_de_compras.html', {
        'compras_usuario': compras_usuario
    })

@login_required(login_url='login')
def delete_offer(request, pk_offer):
    
    oferta = Oferta.objects.get(id=pk_offer)
    oferta.is_active = False
    oferta.save()

    return redirect('published_offers', pk_usuario=request.user.id)

@login_required(login_url='login')
def articulo_comprado(request):
    return render(request, 'articulo_comprado.html')

@login_required(login_url='login')
def mensajes(request):
    mensajes_usuario = Mensaje.objects.filter(receptor=request.user.id, visto=False)
    # Form de mensajes
    form_mensaje = formMensaje()

    if request.method == 'POST':
        form = formMensaje(request.POST)
        if form.is_valid():
            mensaje = Mensaje.objects.get(id=request.POST['mensaje_or'])
            form.instance.emisor = request.user
            form.instance.receptor = mensaje.emisor
            form.instance.oferta = mensaje.oferta
            form.save()
            messages.success(request, 'Tu respuesta ha sido enviada con éxito.')
            return render(request, 'mensajes.html', {
                'mensajes': mensajes_usuario,
                'formMensaje': form_mensaje
            })
        else:
            return HttpResponse(form.errors)    

    return render(request, 'mensajes.html', {
        'mensajes': mensajes_usuario,
        'formMensaje': form_mensaje
    })

@login_required(login_url='login')
def mensaje_visto(request, pk_mensaje):
    mensaje = Mensaje.objects.get(id=pk_mensaje)
    mensaje.visto = True
    mensaje.save()
    
    return redirect('mensajes')