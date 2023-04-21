from django.db import models
from django.conf import settings


from django.contrib.auth.models import User

class Subscriber(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.PositiveIntegerField()
    total = models.DecimalField(max_digits=10, decimal_places=2)
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('ready', 'Ready'),
        ('cancelled', 'Cancelled'),
        ('rejected', 'Rejected'),
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    # seller_name = models.CharField(max_length=50)
    seller_name = models.CharField(max_length=51, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username} - {self.product.name} - {self.status}'


class Product(models.Model):
    CATEGORIES = (
        ('general_store', 'General Store'),
        ('snacks', 'Snacks'),
        ('sweets', 'Sweets'),
        ('electronics', 'Electronics'),
        ('fruits', 'Fruits'),
        ('vegetables', 'Vegetables'),
        ('dairy', 'Dairy'),
        ('stationary', 'Stationary'),
        ('toys', 'Toys'),
        ('gifts', 'Gifts'),
        ('watch', 'Watch'),
        ('drinks', 'Drinks'),
        ('clothings', 'Clothings'),
 
    )
  
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=True, blank=True) 
    selling_price = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True)
    price = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True)
    image = models.ImageField(upload_to='storable-media/', null=True, blank=True)
    is_active = models.BooleanField(default=True, null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    meta_keywords = models.CharField(max_length=255, help_text='Comma-delimited set of SEO keywords for meta tag', null=True, blank=True)
    categories = models.CharField(max_length=50, choices=CATEGORIES, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True) 
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta: 
        db_table = 'products'
        ordering = ['-updated_at']

    def __unicode__(self):
        return self.name
