from django.urls import path

from . import views

app_name = 'homepage'

def tie(ruta, vista, name=None):
    return path(ruta, vista, name=name or vista.__name__)


urlpatterns = [
    tie('', views.homepage),
    ]

