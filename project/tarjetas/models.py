from django.db import models

# Create your models here.

class Tarjetas(models.Model):
    """Definicion de Tarjetas"""
    DEBITO = 'débito'
    CREDITO = 'crédito'
    NINGUNO = ' '
    TIPO_CHOICES = [
        (DEBITO, 'Débito'),
        (CREDITO, 'Crédito'),
        (NINGUNO, ' '),
    ]

    nombre = models.CharField(max_length=25)
    tipo = models.CharField(max_length=25, choices=TIPO_CHOICES, null=True, blank=True)

    def __str__(self) -> str:
        return self.nombre
    
    class Meta:
        verbose_name = "Tarjeta"
        verbose_name_plural = "Tarjetas"