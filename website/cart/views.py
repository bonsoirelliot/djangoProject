from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
# from website.main.models import Book
from .cart import Cart
# from .forms import CartAddProductForm
from django.apps import apps


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    bookModel = apps.get_model('main.Book')
    book = get_object_or_404(bookModel, id=product_id)
    # form = CartAddProductForm(request.POST)
    cart.add(product=book)
    # if form.is_valid():
    #     cd = form.cleaned_data
    #     cart.add(product=book,
    #              quantity=cd['quantity'],
    #              update_quantity=cd['update'])
    return redirect('cart-detail')


def cart_remove(request, product_id):
    cart = Cart(request)
    book = apps.get_model('main.Book')
    product = get_object_or_404(book, id=product_id)
    cart.remove(product)
    return redirect('cart-detail')


def cart_detail(request):
    cart = Cart(request)
    return render(request, 'detail.html', {'cart': cart})
