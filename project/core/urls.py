from django.urls import path

from . import views 
#se usan importaciones relativas con un .

urlpatterns = [
    path("", views.home),
]
