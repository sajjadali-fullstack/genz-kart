from django.shortcuts import render, redirect
from store.forms import CustomUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout  # for login
from store.models import Product,Cart
from django.http import JsonResponse


# Add To Cart
def add_to_cart_view(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            prod_id = int(request.POST.get('product_id'))
            product_check = Product.objects.get(id=prod_id)
            if(product_check):
                if(Cart.objects.filter(user=request.user.id, product_id=prod_id)):
                    return JsonResponse({'status': "Product Already in Cart!"})
                
                else:
                    prod_qty = int(request.POST.get('product_qty'))
                    # If the user is requesting 5 of that product but we have only 3 then we are going to show him msg only this is available
                    if product_check.quantity >= prod_qty:
                        Cart.objects.create(user=request.user, product_id=prod_id, product_qty=prod_qty)
                        return JsonResponse({'status': "Product Added Sucessfully!"})
                    else:
                        # If the prod QTY < than the request QTY
                        return JsonResponse({'status':"Only" + str(product_check.quantity) + " Quantity available"})



            else:
                return JsonResponse({'status': "No Such Product Found!"})
        else:
            return JsonResponse({'error': 'You need to login first!'})
    return redirect('/')



# View Cart

def view_cart(request):
    cart = Cart.objects.filter(user=request.user)
    context = {'cart':cart}
    return render(request, 'store/cart.html', context)


# Update cart
def update_cart_view(request):
    if request.method == 'POST':
        # Fetch:- product id,
        prod_id = int(request.POST.get('product_id'))
        if(Cart.objects.filter(user=request.user, product_id=prod_id)):
            # if product exist in the user cart
            prod_qty = int(request.POST.get('product_qty'))
            cart = Cart.objects.get(product_id=prod_id, user=request.user)
            cart.product_qty = prod_qty
            cart.save()
            return JsonResponse({'status': "Product Updated Sucessfully!"})
        else:
            return JsonResponse({'error': "Product Not Found!"})
        
    return redirect('/')


# Delete Cart Item
def delete_cart_item(request):
    if request.method == 'POST':
        prod_id = int(request.POST.get('product_id'))
        if(Cart.objects.filter(user=request.user, product_id=prod_id)):
            cart_item = Cart.objects.get(product_id=prod_id, user=request.user)
            cart_item.delete()

        return JsonResponse({'status': "Product Deleted Sucessfully!"})
        # else:
        #     return JsonResponse({'error': "Product Not Found!"})
    # if sombody accessing without POST method it will redirect to the homer page
    return redirect('/')