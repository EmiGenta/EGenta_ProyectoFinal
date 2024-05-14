from django.contrib import admin

# Register your models here.
from . import models

admin.site.site_title = "Bancos"

class BancoAdmin(admin.ModelAdmin):
    list_display = (
        "nombre",
        "web",
    )

    list_display_links = ("nombre",)
    search_fields = ("nombre",)
    ordering = ("nombre",)


admin.site.register(models.Bancos, BancoAdmin)