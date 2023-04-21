from django.urls import path
from . import views
from .views import create_product

app_name='catalog'

urlpatterns = [
    path('add-p/', views.addp, name='addp'),
    # path('create-product/', create_product.as_view(), name='create_product'),
    path('create-product/', views.create_product, name='create_product'),
    path('view-p/', views.viewp, name='viewp'),

    
    
    
]
