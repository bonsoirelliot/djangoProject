from django.urls import path
from . import views


urlpatterns = [
    path('', views.cart_detail, name='cart-detail'),
    path('add/<product_id>', views.cart_add, name='cart-add'),
    path('remove/<product_id>', views.cart_remove, name='cart-remove'),
]