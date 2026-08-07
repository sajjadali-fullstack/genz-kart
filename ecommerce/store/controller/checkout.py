from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from store.models import Wishlist, Cart, Order, OrderItem, Profile
from store.models import Product
from django.http import JsonResponse, HttpResponse

import random

from django.contrib.auth.models import User

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

    userprofile = Profile.objects.filter(user=request.user).first()

    context = {'cartitems':cartitems, 'total_price':total_price, 'userprofile':userprofile}

    return render(request, 'store/checkout.html', context)  # render the checkout page



# Place Order
@login_required(login_url='login')
def place_order(request):
    if request.method == 'POST':

        currentuser = User.objects.filter(id=request.user.id).first()

# Store in User model
        if not currentuser.first_name:
            currentuser.first_name = request.POST.get('fname')
            currentuser.last_name = request.POST.get('lname')
            currentuser.save()
# If user placing it order for the first time
        if not Profile.objects.filter(user=request.user).exists():
            userprofile = Profile()
            
            userprofile.user = request.user
            userprofile.phone = request.POST.get('phone')
            userprofile.address = request.POST.get('address')
            userprofile.city = request.POST.get('city')
            userprofile.state = request.POST.get('state')
            userprofile.country = request.POST.get('country')
            userprofile.pincode = request.POST.get('pincode')
            userprofile.save()




        # Get the data from the form
        neworder = Order()
        neworder.user = request.user
        neworder.fname = request.POST.get('fname')
        neworder.lname = request.POST.get('lname')
        neworder.email = request.POST.get('email')
        neworder.phone = request.POST.get('phone')
        neworder.address = request.POST.get('address')
        neworder.city = request.POST.get('city')
        neworder.state = request.POST.get('state')
        neworder.country = request.POST.get('country')
        neworder.pincode = request.POST.get('pincode')

        neworder.payment_mode = request.POST.get('payment_mode')
        neworder.payment_id = request.POST.get('payment_id')


        cart = Cart.objects.filter(user=request.user)
        cart_total_price = 0
        for item in cart:
            cart_total_price += item.product.selling_price * item.product_qty
        neworder.total_price = cart_total_price
        trackno = 'Sajjad' + str(random.randint(1000, 9999))
        while Order.objects.filter(tracking_no=trackno).exists():
            trackno = 'Sajjad' + str(random.randint(1000, 9999))

        neworder.tracking_no = trackno
        neworder.save()

        # Add the order to the database
        neworderitems = Cart.objects.filter(user=request.user)
        for item in neworderitems:
            OrderItem.objects.create(order=neworder, product=item.product, price=item.product.selling_price, quantity=item.product_qty)

            # To decress he product quantity from available stock
            orderproduct = Product.objects.filter(id=item.product_id).first()
            orderproduct.quantity -= item.product_qty
            orderproduct.save()
        # To clear user cart
        Cart.objects.filter(user=request.user).delete()

        messages.success(request, 'Order Placed Successfully')

        pay_mode = request.POST.get('payment_mode')
        if (pay_mode == 'Paid by Razorpay'):
            return JsonResponse({'status':'Your Order Placed has been Successfull'})


    return redirect('home')



# Razorpay Checkout
@login_required(login_url='login')
def razorpaycheck(request):
    # To get the order details
    cart = Cart.objects.filter(user=request.user)
    total_price = 0

    for item in cart:
        total_price += item.product.selling_price * item.product_qty
        
    return JsonResponse({'total_price': total_price})




# My Orders
@login_required(login_url='login')
def my_orders(request):
    return HttpResponse('My Orders Page')