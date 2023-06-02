from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# choices
CALIFICACION_USUARIO_CHOICES = [
    (0,0),
    (1,1),
    (2,2),
    (3,3),
    (4,4)
]

SEXO_USUARIO_CHOICES = [
    ('MASCULINO', 'MASCULINO'),
    ('FEMENINO', 'FEMENINO')
]

# Create your models here.
class UsuarioManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('El usuario debe tener un correo electrónico')
        
        email = self.normalize_email(email)
        usuario = self.model(email=email, **extra_fields)
        usuario.set_password(password)
        usuario.save(using=self._db)

        return usuario


    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)
    
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superusuario debe tener la propiedad "is_staff=True"')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superusuario debe tener la propiedad "is_superuser=True"')
        
        return self._create_user(email, password, **extra_fields)

class Usuario(AbstractBaseUser):
    first_name = models.CharField(verbose_name='Nombre', max_length=255)
    last_name = models.CharField(verbose_name='Apellidos', max_length=255, blank=True, null=True)
    email = models.EmailField(verbose_name='Correo', unique=True, max_length=255)
    cedula = models.CharField(verbose_name='Cédula de Identidad', null=False, blank=False, unique=True, max_length=255)
    telefono = models.CharField(verbose_name='Teléfono', max_length=255, null=False, blank=False, unique=True)
    calificacion = models.SmallIntegerField(verbose_name='Calificación', null=False, blank=False, choices=CALIFICACION_USUARIO_CHOICES, default=0)
    direccion = models.TextField(verbose_name='Dirección', null=True, blank=True)
    foto_perfil = models.ImageField(verbose_name='Foto de perfil', max_length=255, null=True, blank=True, upload_to='perfil/')
    fecha_nacimiento = models.DateField(verbose_name='Fecha de nacimiento', auto_now=False, auto_now_add=False, blank=True, null=True)
    terminos_y_condiciones = models.BooleanField(verbose_name='Términos y condiciones', default=False)
    is_active = models.BooleanField(verbose_name='active',default=True)
    is_staff = models.BooleanField(verbose_name='staff status', default=False)
    is_superuser = models.BooleanField(verbose_name='superuser status', default=False)

    objects = UsuarioManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
    def get_email_user(self):
        return self.email.lower()
    
    def save(self, *args, **kwargs):
        self.email = self.email.lower()
        return super(Usuario, self).save(*args, **kwargs)
    
    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        ordering = ['-id']
