from django.shortcuts import render, redirect
from authentication.forms import FormUsuario

# Create your views here.
def login(request):
    return render(request, 'login.html')

def sign_up(request):
    form_usuario = FormUsuario()
    print('get')
    if request.method == 'POST':
        print('post', request.POST)
        form_usuario = FormUsuario(request.POST)

        if form_usuario.is_valid():

            form_usuario.save()
            return redirect('home')

    return render(request, 'sign_up.html', {
        'form_usuario': form_usuario
    })