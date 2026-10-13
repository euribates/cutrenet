from django.contrib import admin
from django.utils.html import mark_safe

from . import models


class EnlaceAdmin(admin.ModelAdmin):

    class Media:
        css = {
             'all': ('commons/fontawesome/css/all.css',)
            }

    list_display = [
        "titulo_enlace",
        "seccion",
        "entorno",
        "ordenacion",
        'as_icon',
        ]
    list_filter = ['seccion', "entorno"]
    search_fields = [
        'titulo_enlace',
        'texto_ayuda',
        ]

    def as_icon(self, obj):
        if obj.icono:
            return mark_safe(obj.icono)
        return mark_safe('<i>No</i>')


class SeccionAdmin(admin.ModelAdmin):
    list_display = [
        "nombre_seccion",
        "ancho",
        "ordenacion",
        ]
    list_filter = ['nombre_seccion']
    search_fields = [
        'nombre_seccion',
        ]

admin.site.register(models.Seccion, SeccionAdmin)

admin.site.register(models.Enlace, EnlaceAdmin)

