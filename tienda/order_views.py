from django.shortcuts import render
from .models import Order, OrderItem
from .cart.cart import Cart
from django.contrib.auth.decorators import login_required

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

@login_required
def user_orders(request):
    orders = Order.objects.filter(user=request.user).order_by('-created')
    return render(request, 'tienda/order/history.html', {'orders': orders})