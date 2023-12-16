

from django.urls import path
from . import views

app_name = "cliente"

urlpatterns = [
    path("", views.home, name="index"),
    path("crear_pais/", views.crear_pais, name="crear_pais"),
    path("crear_cliente/", views.crear_cliente, name="crear_cliente"),
    
]


# cliente/urls.py

from django.urls import path
from . import views

app_name = "cliente"

urlpatterns = [
    path("", views.home, name="index"),
    path("crear_pais/", views.crear_pais, name="crear_pais"),
    path("crear_cliente/", views.crear_cliente, name="crear_cliente"),
    path("buscar_cliente/", views.buscar_cliente, name="buscar_cliente"),  
   
]
