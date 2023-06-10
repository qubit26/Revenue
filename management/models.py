from django.db import models
from authentication.models import Usuario

# Choices
MATERIAL_CHOICES = [
    ('PLÁSTICO', 'PLÁSTICO'),
    ('VIDRIO', 'VIDRIO'),
    ('PAPEL', 'PAPEL'),
    ('CARTÓN', 'CARTÓN'),
    ('METAL', 'METAL'),
    ('OTROS', 'OTROS')
]

# Create your models here.
class ImagenesOferta(models.Model):
    imagen = models.ImageField(verbose_name='Imagen Oferta', blank=False, null=False, upload_to='img_ofertas/')

    class Meta:
        verbose_name = 'Imagen de Oferta'
        verbose_name_plural = 'Imagenes de Ofertas'
        ordering = ['-id']

class Oferta(models.Model):
    titulo = models.CharField(verbose_name='Título', max_length=100, null=False, blank=False)
    descripcion = models.TextField(verbose_name='Descripción', null=True, blank=True)
    cantidad = models.PositiveSmallIntegerField(verbose_name='Cantidad', null=False, blank=False, default=1)
    valor = models.DecimalField(verbose_name='Valor', max_digits=3, decimal_places=2, null=False, blank=False)
    material = models.CharField(verbose_name='Material', max_length=20, null=False, blank=False, choices=MATERIAL_CHOICES)
    imagenes = models.ManyToManyField(ImagenesOferta, verbose_name='Imagenes de la Oferta', blank=True)
    usuario = models.ForeignKey(Usuario, verbose_name='Usuario', null=False, blank=False, on_delete=models.CASCADE)
    is_active = models.BooleanField(verbose_name='Activo/Inactivo', default=True)
    vendido = models.BooleanField(verbose_name='Vendido', default=False)
    fecha_creacion = models.DateTimeField(verbose_name='Fecha de Creación', auto_now_add=True)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Oferta'
        verbose_name_plural = 'Ofertas',
        ordering = ['-fecha_creacion']

class Venta(models.Model):
    oferta = models.ForeignKey(Oferta, verbose_name='Oferta', null=False, blank=False, on_delete=models.CASCADE)
    fecha_venta = models.DateTimeField(verbose_name='Fecha de Venta', auto_now_add=True)

    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'
        ordering = ['-fecha_venta']

class Compra(models.Model):
    venta = models.ForeignKey(Venta, verbose_name='Venta', null=False, blank=False, on_delete=models.CASCADE)
    comprador = models.ForeignKey(Usuario, verbose_name='Comprador', null=False, blank=False, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Compra'
        verbose_name_plural = 'Compras'
        ordering = ['-id']
