from management.models import *

def get_notificaciones(request):
    notificaciones = Notificacion.objects.filter(receptor=request.user.id)[:3]
    return {'notificaciones': notificaciones}

def get_mensajes(request):
    mensajes = Mensaje.objects.filter(receptor=request.user.id)[:4]
    return {'mensajes': mensajes}