from django.contrib import admin

# Register your models here.
from . import models

admin.site.site_title = "Tarjetas"

class TarjetaAdmin(admin.ModelAdmin):
    list_display = (
        "nombre",
        "tipo",
    )

    list_display_links = ("nombre",)
    search_fields = ("nombre",)
    ordering = ("nombre",)

class DescuentoAdmin(admin.ModelAdmin):
    list_display = (
        "tarjeta",
        "descripcion",
        "fecha_ingreso",
        "rubro",
        "nombre_local",
        "porcentaje",
    )
    list_display_links = ("nombre_local",)
    search_fields = ("nombre_local", "rubro", "tarjeta__nombre")
    ordering = ("fecha_ingreso",)
    list_filter = ("tarjeta", "rubro")

admin.site.register(models.Tarjetas, TarjetaAdmin)
admin.site.register(models.Descuento, DescuentoAdmin)