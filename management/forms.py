from django import forms
from management.models import ImagenesOferta, Oferta, MATERIAL_CHOICES, Mensaje

class formOferta(forms.ModelForm):

    class Meta:
        model = Oferta
        fields = ('titulo', 'descripcion', 'cantidad', 'valor', 'material')
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
            ),
            'cantidad': forms.NumberInput(
                attrs={
                    'type': 'range',
                    'class': 'form-range w-100',
                    'id': 'cantidad',
                    'min': '1',
                    'max': '100',
                    'steps': '1',
                    'value': '1'
                }
            ),
            'valor': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'id': 'valor',
                    'steps': '0.01',
                    'placeholder': '0.00$'
                }
            ),
            'material': forms.Select(
                attrs={
                    'class': 'custom-select'
                },
                choices=MATERIAL_CHOICES
            )
        }

class formMensaje(forms.ModelForm):
    class Meta:
        model = Mensaje
        fields = ('mensaje',)
        widgets = {
            'mensaje': forms.Textarea(
                attrs={
                    'class': 'form-control w-100',
                    'id': 'mensaje',
                    'placeholder': 'Escribe tu mensaje'
                }
            )
        }