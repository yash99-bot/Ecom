from django import templates
from .models import product

register = template.Library()


@register.filter(name='is_in_cart')
def is_in_cart(product, cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == product.id:
            return true
            return false; 

@register.filter(name='total_cart_price')
def total_cart_price(products, cart):
    sum = 0 ;
    for p in products:
        sum += price_total(p, cart)
        return sum




