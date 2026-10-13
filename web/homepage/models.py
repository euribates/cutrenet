from django.db import models

# Create your models here.

class Seccion(models.Model):

    class Meta:
        verbose_name = "sección"
        verbose_name_plural = "secciones"
        ordering = [
            "ordenacion",
            ]

    id_seccion = models.BigAutoField(primary_key=True)
    nombre_seccion = models.CharField(
        max_length=64,
        unique=True,
        )
    ancho = models.IntegerField(
        default=4,
        help_text="Columnas que ocupará esta sección.",
        )
    ordenacion = models.IntegerField(default=0)

    def __str__(self):
        return self.nombre_seccion


class Enlace(models.Model):

    class Meta:
        verbose_name = "enlace"
        verbose_name_plural = "enlaces"

        ordering = [
            "ordenacion",
            ]
        unique_together = [
            ('entorno', 'titulo_enlace'),
            ('entorno', 'url'),
            ]

    class Entorno(models.TextChoices):
        DEV = ('DEV', "Desarrollo")
        PRE = ('PRE', "Pre-explotación")
        EXP = ('EXP', "Explotación")
        LNK = ('LNK', "Enlace externo")

    id_enlace = models.BigAutoField(primary_key=True)
    titulo_enlace = models.CharField(max_length=1024)
    seccion = models.ForeignKey(
        Seccion,
        on_delete=models.PROTECT,
        )
    texto_ayuda = models.CharField(
        max_length=1024,
        blank=True,
        default='',
        )
    url = models.URLField(
        unique=True,
        max_length=1024,
        )
    entorno = models.CharField(
        max_length=3,
        choices=Entorno,
        default=Entorno.LNK,
        )
    icono = models.CharField(
        max_length=256,
        default='',
        blank=True,
        )
    ordenacion = models.IntegerField(default=0)

    def __str__(self):
        return self.titulo_enlace

    def as_entorno(self):
        match self.entorno:
            case Enlace.Entorno.DEV:
                return '<code class="dev">DEV</code>'
            case Enlace.Entorno.PRE:
                return '<code class="pre">PRE</code>'
            case Enlace.Entorno.EXP:
                return '<code class="exp">EXP</code>'
            case Enlace.Entorno.LNK:
                return ''
            case _:
                return (
                    '<span class="error">'
                    f"ERROR: Entorno {self.entorno} DESCONOCIDO"
                    '<span>'
                    )
