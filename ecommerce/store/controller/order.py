from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from store.models import Order, OrderItem

# My Orders
def order_index(request):
    orders = Order.objects.filter(user=request.user)
    context = {'orders':orders}
    return render(request, 'store/orders/index.html', context)


# View Order
def view_order(request, tracking_no):
    # Verify order belongs to the logged in user
    order = Order.objects.filter(tracking_no=tracking_no).filter(user=request.user).first()
    order_items = OrderItem.objects.filter(order=order)

    context = {
        'order':order,
        'order_items':order_items
        }    
    return render(request, 'store/orders/view.html', context)