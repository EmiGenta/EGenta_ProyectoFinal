from django.urls import path
from . import views

app_name = "bancos"

urlpatterns = [
    path("", views.home, name="home"),
    path("bancos/create/", views.BancosCreate.as_view(), name="bancos_create"),
    path("tarjetas/list/", views.BancosList.as_view(), name="bancos_list"),
]