from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .models import Product
from .cart.cart import Cart

@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.add(product=product, quantity=1)
    return redirect('tienda:cart_detail')

def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('tienda:cart_detail')

def cart_detail(request):
    cart = Cart(request)
    return render(request, 'tienda/cart/detail.html', {'cart': cart})