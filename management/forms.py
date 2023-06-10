from django import forms
from management.models import ImagenesOferta, Oferta

class formOferta(forms.ModelForm):


    class Meta:
        model = Oferta
        fields = ('titulo', 'descripcion', 'cantidad', 'valor')
        widgets = {
            'titulo': forms.TextInput(
                attrs={
                    'class': 'form-control w-100',
                    'id': 'titulo',
                    'placeholder': 'Coloca el título aquí'
                }
            ),
            'descripcion': forms.Textarea(
                attrs={
                    'class': 'form-control w-100',
                    'id': 'descripcion',
                    'placeholder': 'Añade la descripción aquí'
                }
            )
        }