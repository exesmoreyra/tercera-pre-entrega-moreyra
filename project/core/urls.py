from django.urls import path

from . import views 
#se usan importaciones relativas con un .
app_name = "core"

urlpatterns = [
    path("", views.home, name="index"),
]
