from django import template
register = template.Library()
@register.simple_tag()
def simpl_date(date):
    return date.strftime('%d %b')