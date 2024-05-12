from django.db import models

class Bancos(models.Model):
    """Definición de Bancos"""
    nombre = models.CharField(max_length=50, verbose_name="Nombre del Banco")
    web = models.URLField(max_length=200, verbose_name="Sitio Web del Banco")

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Banco"
        verbose_name_plural = "Bancos"
