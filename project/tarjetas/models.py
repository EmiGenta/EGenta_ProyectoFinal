from django.db import models
from django.utils import timezone

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

class Descuento(models.Model):
    RUBRO_CHOICES = [
        ('Vestimenta', 'Vestimenta'),
        ('Calzado', 'Calzado'),
        ('Gastronomía', 'Gastronomía'),
        ('Servicios', 'Servicios'),
        ('Infantiles', 'Infantiles'),
        ('Electrodomésticos', 'Electrodomésticos'),
        ('Tecnología', 'Tecnología'),
        ('Bienestar y Tiempo Libre', 'Bienestar y Tiempo Libre'),
        ('Viajes y Turismo', 'Viajes y Turismo'),
    ]
    
    tarjeta = models.ForeignKey(Tarjetas, on_delete=models.CASCADE)
    descripcion = models.TextField()
    fecha_ingreso = models.DateTimeField(default=timezone.now)
    rubro = models.CharField(max_length=50, choices=RUBRO_CHOICES)
    nombre_local = models.CharField(max_length=100  )
    web_local = models.URLField(null=True, blank=True)
    porcentaje = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.nombre_local} - {self.porcentaje}%"