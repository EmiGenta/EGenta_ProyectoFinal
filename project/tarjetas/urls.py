from django.urls import path
from . import views

app_name = "tarjetas"

urlpatterns = [
    path("", views.home, name="home"),
    path("tarjetas/create/", views.TarjetasCreate.as_view(), name="tarjetas_create"),
    path("tarjetas/list/", views.TarjetasList.as_view(), name="tarjetas_list"),
]