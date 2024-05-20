from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth import login
from django.db import IntegrityError
from django.contrib import messages

from .forms import CustomAuthenticationForm, CustomUserCreationForm

User = get_user_model()

def home(request):
    return render(request, "core/index.html")

class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm
    template_name = "core/login.html"

def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            try:
                user = form.save()
                login(request, user)
                return redirect('core:home')
            except IntegrityError as e:
                if 'UNIQUE constraint failed' in str(e):
                    form.add_error('email', 'El email ya existe. Por favor elige otro.')
                else:
                    form.add_error(None, 'Ocurrió un error. Por favor inténtelo de nuevo.')
    else:
        form = CustomUserCreationForm()
    return render(request, 'core/register.html', {'form': form})