from django.urls import path
from . import views

urlpatterns = [
    path("cart/", views.cart_view),
    path("cart/order/", views.order_view),
    path("cart/delete/", views.cart_delete_view),
    path("login/", views.login_view),
    path("logout/", views.logout_view),
    path("register/", views.register_view),
]
