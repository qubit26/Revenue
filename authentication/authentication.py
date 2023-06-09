from django.contrib.auth.backends import ModelBackend
from authentication.models import Usuario

class UsuarioAuthBackend(ModelBackend):
     def authenticate(self, request, **kwargs):
          email = kwargs['email']
          password = kwargs['password']

          try:
               usuario = Usuario.objects.get(email=email)
               if usuario.check_password(password) is True:
                    return usuario
          except Usuario.DoesNotExist:
               return None