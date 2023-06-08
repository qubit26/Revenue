from django import forms
from django.contrib.auth.forms import AuthenticationForm
from authentication.models import Usuario

# Forms
# class FormularioLogin(AuthenticationForm):
#     def __init__(self, *args, **kwargs):
#         super(FormularioLogin, self).__init__(*args, **kwargs)

class FormUsuario(forms.ModelForm):
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput(
        attrs={
            'class':'form-control form-control-user',
            'placeholder': 'Ingrese una Contraseña',
            'id': 'password1',
            'required': 'required'
        }
    ))
    password2 = forms.CharField(label='Repetir Contraseña', widget=forms.PasswordInput(
        attrs={
            'class':'form-control form-control-user',
            'placeholder': 'Repita la Contraseña',
            'id': 'password2',
            'required': 'required'
        }
    ))

    class Meta:
        model = Usuario
        fields = ('first_name', 'last_name', 'email', 'cedula', 'telefono', 'direccion', 'foto_perfil', 'terminos_y_condiciones')
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'class': 'form-control form-control-user',
                    'placeholder': 'Nombres'
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'class': 'form-control form-control-user',
                    'placeholder': 'Apellidos'
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control form-control-user',
                    'placeholder': 'Ingrese su correo'
                }
            ),
            'cedula': forms.TextInput(
                attrs={
                    'class': 'form-control form-control-user',
                    'placeholder': 'Ingrese su Cédula'
                }
            ),
            'telefono': forms.TextInput(
                attrs={
                    'class': 'form-control form-control-user',
                    'placeholder': 'Ingrese su Teléfono'
                }
            ),
            'direccion': forms.TextInput(
                attrs={
                    'class': 'form-control form-control-user',
                    'placeholder': 'Ingrese su Dirección'}
            ),
            'foto_perfil': forms.FileInput(
                attrs={
                    'class': 'form-control-file'
                }
            ),
            'terminos_y_condiciones': forms.CheckboxInput(
                attrs={
                    'class': 'form-check-input pl-5 ml-3'
                }
            )
        }

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Las contraseñas no son iguales.')
        return password2
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user