from django.shortcuts import render

from . import models

def homepage(request):
    enlaces = (
        models.Enlace.objects
        .select_related('seccion')
        .order_by('seccion__ordenacion', 'ordenacion')
        )

    return render(request, 'homepage/homepage.html', {
        'titulo': "Cutrenet imperial",
        'enlaces': enlaces,
        })
