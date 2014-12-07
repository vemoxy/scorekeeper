from django import template

register = template.Library()

@register.filter
def us_to_space(value):
	return value.replace('_',' ')

@register.filter
def get(dict, key):    
    return dict[key]