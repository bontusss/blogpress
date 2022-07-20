from django import template
import calendar
from datetime import date

register = template.Library()

@register.filter
def month_name(value):
    return calendar.month_abbr[value]


@register.tag
def current_year():
    current_year = date.today().year
    return current_year