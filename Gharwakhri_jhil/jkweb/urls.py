"""jkweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import is_valid_path, include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),

    path('', include('catalog.urls')),
    # path('', include('cartapp.urls')),
    # path('', include('feedback.urls')),
    path('search/', views.search, name='search'),
    # path('sdetails/<int:sid>/', views.sdetails, name='sdetails'),
    path('catalog/<int:id>/', views.product_detail, name='product_detail'),
    path('cancel_order/<int:pk>/', views.cancel_order, name='cancel_order'),
    # path('product/',include('products.urls')),
    path('signup/', views.signup, name='signup'),
    path('loginin/', views.loginin, name='loginin'),
    path('logout/', views.logout, name='logout'),
    
    path('page-about/', views.pgabout, name='pgabout'),
    path('buyer-home/',views.buyerhome, name='buyerhome'),
    path('private-policy/',views.privatepolicy,name='privatepolicy'),
    path('purchase-guide/',views.purchaseguide,name='purchaseguide'),
    path('page-terms/',views.pgterms,name='pgterms'),
    path('help-center/',views.helpcenter,name='helpcenter'),
    # path('add-product/', views.addproduct, name='addproduct'),  # IN PRODUCT APP      
    path('seller-home/', views.sellerhome, name='sellerhome'),
    path('seller-profile/', views.sellerprofile, name='sellerprofile'),#26th march 12.14am
    path('seller-order/', views.seller_order, name='seller_order'),
    path('only-order/', views.only, name='only'),
    path('product/<int:pk>/', views.delete_product, name='delete_product'),
    
    path('products/<int:product_id>/edit/', views.edit_product, name='edit_product'),
    
    path('deactivate/', views.deactivate_account, name='deactivate_account'),
    path('vendors/', views.vendor_list, name='vendor_list'),
    
    path('orders/<int:pk>/action/', views.order_action, name='order_action'),
    # path('orders/<int:pk>/', views.confirm_order, name='confirm_order'),
    # path('orders/<int:pk>/', views.reject_order, name='reject_order'),
    # path('orders/<int:pk>/', views.ready_order, name='ready_order'),
    
    path('buyer-order-page/', views.buyer_order, name='buyer_order'),
    path('order-page/', views.orderpage, name='orderpage'),
    
 
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
handler404 = 'jkweb.views.file_not_found_404'







# from django.conf import settings
# from django.db import models

# class Profile(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # other fields
    # 
    # from accounts.models import CustomUser
    
    


# from accounts.models import CustomUser

# my_user = CustomUser.objects.get(id=1)


# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', views.home, name='home'),
#     path('register/', views.showformdata, name='register'),
    
#     path('page-pglogin/', views.my_view, name='pglogin'),
#     path('page-register/', views.add_user, name='add_user'),
#     # path('page-loginin/', views.loginin, name='loginin'),    
#     path('page-about/', views.pgabout,name='pgabout'),
#     # path('page-register/', views.pgregister, name='pgregister'),
    
#     # path('blog-category-list/',views.blogcategorylist,name='blogcategorylist'),
#     # path('blog-post-left/', views.blogpostleft,name='blogpostleft'),
#     # path('blog-post-right/',views.blogpostright,name='blogpostright'),
    
    
#     path('page-account/', views.pgaccount, name='pgaccount'),
    
#     path('page-contact/',views.pgcontact,name='pgcontact'),
#     path('page-pvt-policy/',views.pgpvtpolicy,name='pgpvtpolicy'),
#     path('page-purchase-guide/',views.purchaseguide,name='purchaseguide'),
    
#     path('shop-cart/',views.shopcart,name='shopcart'),
#     # path('shop-compare/',views.shopcompare,name='shopcompare'),
#     # path('shop-grid-left/',views.shopgridleft,name='shopgridleft'),
#     # path('shop-invoice/',views.shopinvoice,name='shopinvoice'),
#     # path('shop-grid-right/',views.shopgridright,name='shopgridright'),
#     # path('shop-list-left/',views.shoplistleft,name='shoplistleft'),
#     # path('shop-list-right/',views.shoplistright,name='shoplistright'),
#     path('shop-wishlist/',views.shopwish,name='shopwish'),
    
# ]
