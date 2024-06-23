from django import template

register = template.Library()   # decorator

@register.filter(name='currency')
def currency(number):
    return "₹ "+str(number)



@register.filter(name='multiply')
def multiply(number, number1):
    return number * number1