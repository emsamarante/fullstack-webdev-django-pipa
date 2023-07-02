from django import template
from django.utils import formats

register = template.Library()


@register.filter
def format_date_pt(value):
    return value.strftime("%d de %B de %Y")

