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

# Creo el home de Tarjetas
# def home(request):
#     consulta = request.GET.get("consulta", None)
#     form = forms.TarjetasForm()
#     if consulta:
#         print(consulta)
#         query = models.Tarjetas.objects.filter(nombre__icontains=consulta)
#     else:
#         query = models.Tarjetas.objects.all()
#     context = {"tarjetas": query, "form": form} #consulta a la bdd
#     return render(request, "tarjetas/index.html", context)

def home(request):
    return render(request, "tarjetas/index.html")

class TarjetasList(ListView):
    model = models.Tarjetas

    # context_object_name = "productos"
    # template_name = "producto/productocategoria___list.html"

    def get_queryset(self) -> QuerySet:
        if self.request.GET.get("consulta"):
            consulta = self.request.GET.get("consulta")
            object_list = models.Tarjetas.objects.filter(nombre__icontains=consulta)
        else:
            object_list = models.Tarjetas.objects.all()
        return object_list

class TarjetasCreate(CreateView):
    model = models.Tarjetas
    form_class = forms.TarjetasForm
    success_url = reverse_lazy("tarjetas:home")