from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
def as_entorno(entorno) -> str:
    match entorno:
        case 'DEV':
            return mark_safe('<code class="dev">DEV</code>')
        case 'PRE':
            return mark_safe('<code class="pre">PRE</code>')
        case 'EXP':
            return mark_safe('<code class="exp">EXP</code>')
        case 'LNK':
            return ''
        case _:
            return mark_safe(
                '<span class="error">'
                f"ERROR: Entorno <code>{entorno}</code> desconocido"
                '<span>'
                )
