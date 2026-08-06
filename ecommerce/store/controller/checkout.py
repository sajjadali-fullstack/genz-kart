from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from store.models import Wishlist, Cart
from store.models import Product



# Checkout Page
@login_required(login_url='login')
def index(request):
    rawcart = Cart.objects.filter(user=request.user)
# Only product which are available in stock that things are remaining in our cart 
    for item in rawcart:
        if item.product_qty > item.product.quantity:
            Cart.objects.filter(id=item.id).delete()
            
    cartitems = Cart.objects.filter(user=request.user)
    total_price = 0

    for item in cartitems:
        total_price += item.product.selling_price * item.product_qty

    context = {'cartitems':cartitems, 'total_price':total_price}

    return render(request, 'store/checkout.html', context)  # render the checkout page