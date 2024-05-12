from django import forms
from . import models

class BancosForm(forms.ModelForm):
    class Meta:
        model = models.Bancos
        fields = "__all__"
        labels = {
            "nombre": "Nombre del Banco",
            "web": "Página Web del Banco",
        }
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control", "placeholder": "Ingrese el nombre del banco"}),
            "web": forms.URLInput(attrs={"class": "form-control", "placeholder": "Ingrese la página web del banco"}),
        }