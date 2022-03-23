from django import template


register = template.Library()

def bold_value(value, arg):
	if arg in value:
		value = value.replace(arg, "<strong>"+arg+"</strong>")
	print(value)
	return value

def update_value(value, arg):
	value = arg
	return value

register.filter('bold_value', bold_value)
register.filter('update_value', update_value)