from django import forms
from . import models

class TarjetasForm(forms.ModelForm):
    class Meta:
        model = models.Tarjetas
        fields = "__all__"
        widgets = {
            "Nombre": forms.TextInput(attrs={"class": "form-control"}),
            "tipo": forms.Select(choices=models.Tarjetas.TIPO_CHOICES, attrs={"class": "form-control"}),
        }