from django.contrib import admin
from .models import Cart,CartProduct


class CartAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "count", "total_price"]

class CartProductAdmin(admin.ModelAdmin):
    list_display = ["product", "quantity", "total_price"]


admin.site.register(Cart, CartAdmin)
admin.site.register(CartProduct, CartProductAdmin)
