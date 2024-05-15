from django.urls import path
from . import views

app_name = "bancos"

urlpatterns = [
    path("", views.home, name="home"),
    path("bancos/create/", views.BancosCreate.as_view(), name="bancos_create"),
    path("bancos/list/", views.BancosList.as_view(), name="bancos_list"),
    path("bancos/detail/<int:pk>", views.BancosDetail.as_view(), name="bancos_detail"),
    path("bancos/update/<int:pk>", views.BancosUpdate.as_view(), name="bancos_update"),
]
