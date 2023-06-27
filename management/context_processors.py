from management.models import *

def get_notificaciones(request):
    notificaciones = Notificacion.objects.filter(receptor=request.user.id)[:3]
    no_vistas = Notificacion.objects.filter(receptor=request.user.id, visto=False).count()
    return {
        'notificaciones': notificaciones,
        'no_vistas': no_vistas
        }

def get_mensajes(request):
    mensajes = Mensaje.objects.filter(receptor=request.user.id)[:4]
    no_vistos = Mensaje.objects.filter(receptor=request.user.id, visto=False).count()
    return {
        'mensajes': mensajes,
        'no_vistos': no_vistos
        }