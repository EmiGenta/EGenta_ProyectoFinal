from django.db import models

# Create your models here.

class Tarjeta(models.Model):
    """Definicion de Tarjetas"""
    DEBITO = 'débito'
    CREDITO = 'crédito'
    TIPO_CHOICES = [
        (DEBITO, 'Débito'),
        (CREDITO, 'Crédito'),
    ]

    nombre = models.CharField(max_length=25)
    tipo = models.CharField(max_length=25, choices=TIPO_CHOICES, null=True)

    def __str__(self) -> str:
        return self.nombre
    
    class Meta:
        verbose_name = "Tarjeta"
        verbose_name_plural = "Tarjetas"