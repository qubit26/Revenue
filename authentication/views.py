from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from authentication.authentication import UsuarioAuthBackend
from django.shortcuts import render, redirect
from authentication.forms import FormUsuario

# Create your views here.
def login(request):

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        print(request.POST)

        u = UsuarioAuthBackend()
        usuario = u.authenticate(request=request, email=email, password=password)
        print(usuario)
        if usuario is not None:
            auth_login(request, usuario, backend='authentication.authentication.UsuarioAuthBackend')
            return redirect('home')
        
    return render(request, 'login.html')

def sign_up(request):

    if request.user.is_authenticated:
        return redirect('home')

    form_usuario = FormUsuario()
    
    if request.method == 'POST':
        
        form_usuario = FormUsuario(request.POST)

        if form_usuario.is_valid():

            form_usuario.save()
            return redirect('home')
        return form_usuario.errors

    return render(request, 'sign_up.html', {
        'form_usuario': form_usuario
    })

def logout(request):
    auth_logout(request)
    return redirect('login')