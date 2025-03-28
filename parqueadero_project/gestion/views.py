# gestion/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import transaction

def custom_login(request):
    if request.user.is_authenticated:
        return redirect('main')
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('main')
        else:
            messages.error(request, "Credenciales inválidas.")
    return render(request, 'gestion/login.html')

@login_required
def main_view(request):
    # Obtenemos el rol del usuario; se asume que el campo rol ya está asignado
    rol = request.user.rol.nombre_rol if request.user.rol else 'USUARIO_NORMAL'
    context = {
        'nombre_usuario': request.user.username,
        'rol': rol,
    }
    return render(request, 'gestion/main.html', context)

def logout_view(request):
    logout(request)
    return redirect('login')
