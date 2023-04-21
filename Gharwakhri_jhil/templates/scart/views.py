from django.shortcuts import render
from scart.cart import cart

import random
 
def _generate_cart_id():
     cart_id = ''
     characters = 'ABCDEFGHIJKLMNOPQRQSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()'
     cart_id_length = 50
     for y in range(cart_id_length):
          cart_id += characters[random.randint(0, len(characters)-1)] 
     return cart_id


def _cart_id(request): 
     if  'cart_id' in request.session:
          request.session['cart_id'] = _generate_cart_id() 
     return request.session['cart_id']


def show_cart(request, template_name="buyer/cart-page.html"): 
     cart_item_count = cart.cart_item_count(request)
     page_title = 'Shopping Cart' 
     context = {
         'cart_item_count': cart_item_count,
         'page_title': page_title,
     }
     return render(request, template_name, context)