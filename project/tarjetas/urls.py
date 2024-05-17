from django.urls import path
from . import views

app_name = "tarjetas"

# Tarjetas
urlpatterns = [
    path("", views.home, name="home"),
    path("tarjetas/create/", views.TarjetasCreate.as_view(), name="tarjetas_create"),
    path("tarjetas/list/", views.TarjetasList.as_view(), name="tarjetas_list"),
    
]

# Descuentos
urlpatterns += [
    path('<int:pk>/descuentos/', views.DescuentoListView.as_view(), name='descuentos_list'),
    path('<int:pk>/descuentos/nuevo/', views.DescuentoCreateView.as_view(), name='descuento_create'),
    path('descuentos/<int:pk>/editar/', views.DescuentoUpdateView.as_view(), name='descuento_update'),
    path('descuentos/<int:pk>/eliminar/', views.DescuentoDeleteView.as_view(), name='descuento_delete'),
]
