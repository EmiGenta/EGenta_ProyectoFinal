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

class DescuentoForm(forms.ModelForm):
    class Meta:
        model = models.Descuento
        fields = ['tarjeta', 'descripcion', 'rubro', 'nombre_local', 'web_local', 'porcentaje']
        widgets = {
            'tarjeta': forms.Select(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'rubro': forms.Select(attrs={'class': 'form-control'}),
            'nombre_local': forms.TextInput(attrs={'class': 'form-control'}),
            'web_local': forms.URLInput(attrs={'class': 'form-control'}),
            'porcentaje': forms.NumberInput(attrs={'class': 'form-control'}),
        }