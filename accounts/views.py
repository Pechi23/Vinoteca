from django.shortcuts import render,redirect
from django.contrib.auth import login,logout
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Cart
import random


def register_view(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        user_obj = form.save()
        return redirect('/accounts/login/')
    context = {
        "form": form,
    }
    return render(request, "register.html", context=context)

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect("/")
    else:
        form = AuthenticationForm(request)

    context = {
        "form":form,
    }
    return render(request, "login.html",context=context)

@login_required
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect("/")
    return render(request, "logout.html")

@login_required
def cart_view(request):
    try:
        cart = Cart.objects.get(user=request.user)
    except:
        cart = Cart(user=request.user)
        cart.save()

    context = {
        "cart":cart,
    }
    return render(request, "cart.html", context=context)

@login_required
def cart_delete_view(request):
    cart = Cart.objects.get(user=request.user)
    cart.products.clear()
    cart.save()
    return redirect("/accounts/cart/")

@login_required
def order_view(request):
    cart = Cart.objects.get(user=request.user)
    cart.save()
    #russian rullete for order succes (with 1/3 fail rate)
    ordered = True
    rand_int = random.randint(1,3)
    if rand_int == 3:
        ordered = False

    context = {
        "succes": ordered,
    }

    return render(request,"order.html", context=context)



