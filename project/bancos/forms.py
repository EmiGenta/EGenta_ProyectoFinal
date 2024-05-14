from django import forms
from . import models

class BancosForm(forms.ModelForm):
    class Meta:
        model = models.Bancos
        fields = "__all__"
        labels = {
            "nombre": "Nombre del Banco",
            "web": "Página Web del Banco",
            "pais_origen": "País de Origen",
            "casa_central": "Casa Central",
            "mail_contacto": "Email de Contacto",
        }
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control", "placeholder": "Ingrese el nombre del banco"}),
            "web": forms.URLInput(attrs={"class": "form-control", "placeholder": "Ingrese la página web del banco"}),
            "pais_origen": forms.TextInput(attrs={"class": "form-control", "placeholder": "Ingrese el país de origen del banco"}),
            "casa_central": forms.TextInput(attrs={"class": "form-control", "placeholder": "Ingrese la casa central del banco"}),
            "mail_contacto": forms.EmailInput(attrs={"class": "form-control", "placeholder": "Ingrese el email de contacto"}),
        }