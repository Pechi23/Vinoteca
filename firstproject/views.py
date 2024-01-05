from django.shortcuts import render
from django.http import HttpResponse
from accounts.models import Cart


def home_view(request):
    if request.user.is_authenticated:
        try:
            cart = Cart.objects.get(user=request.user)
        except:
            if request.user.is_authenticated:
                cart = Cart(user=request.user)
                cart.save()
    return render(request, "home-view.html", context=None)
