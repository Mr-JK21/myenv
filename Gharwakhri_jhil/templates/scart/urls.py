from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_cart, {'template_name': 'products/cart-page.html'}, name='showcart'),
]
