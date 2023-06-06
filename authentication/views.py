from django.shortcuts import render, redirect

# Create your views here.
def login(request):
    return render(request, 'login.html')

def sign_up(request):
    return render(request, 'sign_up.html')