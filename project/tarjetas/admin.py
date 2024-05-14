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


admin.site.register(models.Tarjetas, TarjetaAdmin)