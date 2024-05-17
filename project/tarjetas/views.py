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
    context_object_name = "tarjetas"

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

class DescuentoListView(ListView):
    model = models.Descuento
    template_name = 'tarjetas/descuentos_list.html'
    context_object_name = 'descuentos'

    def get_queryset(self):
        return models.Descuento.objects.filter(tarjeta_id=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tarjeta'] = models.Tarjetas.objects.get(pk=self.kwargs['pk'])
        return context

class DescuentoCreateView(CreateView):
    model = models.Descuento
    form_class = forms.DescuentoForm
    template_name = 'tarjetas/descuento_form.html'
    success_url = reverse_lazy('tarjetas:tarjetas_list')

    def get_initial(self):
        initial = super().get_initial()
        initial['tarjeta'] = self.kwargs['pk']
        return initial

class DescuentoUpdateView(UpdateView):
    model = models.Descuento
    form_class = forms.DescuentoForm
    template_name = 'tarjetas/descuento_form.html'
    success_url = reverse_lazy('tarjetas:tarjetas_list')

class DescuentoDeleteView(DeleteView):
    model = models.Descuento
    template_name = 'tarjetas/descuento_confirm_delete.html'
    success_url = reverse_lazy('tarjetas:tarjetas_list')    