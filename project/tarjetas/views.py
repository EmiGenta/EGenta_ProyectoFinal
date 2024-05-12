from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.db.models.query import QuerySet
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from . import forms, models
from .models import Tarjetas

def home(request):
    consulta = request.GET.get("consulta")
    if consulta:
        tarjetas = Tarjetas.objects.filter(nombre__icontains=consulta)
    else:
        tarjetas = Tarjetas.objects.all()
    return render(request, "tarjetas/index.html", {"tarjetas": tarjetas})

class TarjetasList(ListView):
    model = models.Tarjetas
    template_name = "tarjetas/index.html"
    context_object_name = "object_list"  # Cambiado de 'tarjetas' a 'object_list'

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.GET.get("consulta"):
            consulta = self.request.GET.get("consulta")
            queryset = queryset.filter(nombre__icontains=consulta)
        return queryset

class TarjetasCreate(CreateView):
    model = models.Tarjetas
    form_class = forms.TarjetasForm
    success_url = reverse_lazy("tarjetas:home")