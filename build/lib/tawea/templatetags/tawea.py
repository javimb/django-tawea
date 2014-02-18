from django import template


register = template.Library()


@register.inclusion_tag('tawea/tawea.html')
def tawea(**kwargs):
    """
    {% tawea [color=<hex_color>] %}
    """
    color = kwargs.get('color')
    context = {}
    context['color'] = color if color else '#3b5998'
    return context
