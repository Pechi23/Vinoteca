from django.db import models
from django.utils.text import slugify

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    slug = models.SlugField(max_length=50, null=True, blank=True)
    description = models.CharField(max_length=400, null=True, blank=True)
    available = models.BooleanField(default=True)
    year = models.PositiveIntegerField(null=True, blank=True)
    country = models.CharField(max_length=50, null=True, blank=True)
    discount = models.PositiveIntegerField(null=True, blank=True)

    @property
    def tax(self):
        tax = self.price_after_discount * 19/100
        return round(tax, 2)
    
    @property
    def price_after_discount(self):
        if self.discount is not None:
            result = self.price * (100-self.discount)/100
        else:
            result = self.price
        return round(result, 2)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        self.price = round(self.price, 2)
        super().save(*args, **kwargs)
