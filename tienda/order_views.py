from django.shortcuts import render
from .models import Order, OrderItem
from .cart.cart import Cart

def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        order = Order.objects.create(user=request.user)
        for item in cart:
            OrderItem.objects.create(
                order=order,
                product=item['product'],
                price=item['price'],
                quantity=item['quantity']
            )
        cart.clear()
        return render(request, 'tienda/order/created.html', {'order': order})
    return render(request, 'tienda/cart/detail.html', {'cart': cart})