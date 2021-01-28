from django import template

register = template.Library()

@register.filter
def three_dot(value):
    return value.replace("&#8230;","...")
    