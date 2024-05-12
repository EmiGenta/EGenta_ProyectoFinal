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
from .models import Bancos

def home(request):
    consulta = request.GET.get("consulta")
    if consulta:
        bancos = Bancos.objects.filter(nombre__icontains=consulta)
    else:
        bancos = Bancos.objects.all()
    return render(request, "bancos/index.html", {"bancos": bancos})

class BancosList(ListView):
    model = models.Bancos
    template_name = "bancos/index.html"
    context_object_name = "object_list"

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.GET.get("consulta"):
            consulta = self.request.GET.get("consulta")
            queryset = queryset.filter(nombre__icontains=consulta)
        return queryset

class BancosCreate(CreateView):
    model = models.Bancos
    form_class = forms.BancosForm
    success_url = reverse_lazy("bancos:home")