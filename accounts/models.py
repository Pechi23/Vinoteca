from django.db import models
from django.conf import settings
from products.models import Product
# Create your models here.

USER = settings.AUTH_USER_MODEL

class CartProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name = "cart_products")
    quantity = models.PositiveIntegerField(default=1)
    
    @property
    def total_price(self):
        if self.product.discount is not None:
            total = self.product.price_after_discount * self.quantity
        else:
            total = self.product.price * self.quantity
        return round(total,2)

class Cart(models.Model):
    user = models.ForeignKey(USER, on_delete = models.CASCADE)
    products = models.ManyToManyField(CartProduct)


    @property
    def total_price(self):
        total = sum(product.total_price for product in self.products.all())
        return round(total,2)
    
    @property
    def free_shipping(self):
        return self.total_price >= 100
    
    @property
    def taxes(self):
        tax = self.total_price * 19/100
        return round(tax,2)

    @property
    def count(self):
        count = sum(product.quantity for product in self.products.all())
        return count


    


