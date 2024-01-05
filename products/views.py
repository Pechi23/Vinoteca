from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from accounts.models import Cart,CartProduct
from django.db.models import Q
from .models import Product

def products_list_view(request):
    query_dict = request.GET
    query = query_dict.get('q')

    qs = Product.objects.all()
    if query is not None:
        qs = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query) | Q(country__icontains=query))
    context = {
        "products":qs,
    }
    return render(request,"products-list.html",context=context)

@login_required
def product_view(request, slug=None):
    context = {}
    if slug is not None:
            context['product'] = Product.objects.get(slug=slug)
    if request.method == "POST" :
        cart = Cart.objects.get(user=request.user)
        try:
            cart_product = CartProduct.objects.filter(cart=cart).get(product=context['product'])
            if cart_product is not None:
                cart_product.quantity = cart_product.quantity + 1
                cart_product.save()
        except:
            new_cart_product = CartProduct(product=context['product'],cart=cart,quantity=1)
            new_cart_product.save()
            
        return redirect("/products/")
        
    return render(request,"product-view.html", context=context)