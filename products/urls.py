from django.urls import path
from . import views

urlpatterns = [
    path("", views.products_list_view),
    path("<slug:slug>", views.product_view),
]