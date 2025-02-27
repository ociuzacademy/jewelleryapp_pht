from django.db import models

# Create your models here.
class tbl_admin(models.Model):
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.email


from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)
    picture = models.ImageField(upload_to='category_pictures/',null=True,blank=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
from django.db import models
from decimal import Decimal

from django.db import models
from decimal import Decimal

class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='products')
    description = models.TextField(blank=True, null=True)
    size = models.CharField(max_length=50, blank=True, null=True)
    stock = models.PositiveIntegerField(default=0)
    gram = models.CharField(max_length=50, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.name} - {self.category.name} - ${self.price}"

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='product_images/')

    def __str__(self):
        return f"Image for {self.product.name}"
