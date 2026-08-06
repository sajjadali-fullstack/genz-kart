from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from store.models import Wishlist
from store.models import Product




# Wishlist Index
@login_required(login_url='login')
def index(request):
    wishlist = Wishlist.objects.filter(user=request.user).order_by('-created_at')
    context  = {'wishlist':wishlist}
    return render(request, 'store/wishlist.html', context)


# Add to Wishlist
def add_to_wishlist(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            prod_id = int(request.POST.get('product_id'))  
            product_check = Product.objects.get(id=prod_id)  # if product exist in the user wishlist
            if(product_check):
                if Wishlist.objects.filter(user=request.user, product_id=prod_id):
                    return JsonResponse({'status': "Product Already in Wishlist!"})
                else:
                    Wishlist.objects.create(user=request.user, product_id=prod_id)
                    return JsonResponse({'status': "Product Added Sucessfully!"})
            else:
                return JsonResponse({'status': "Product Not Found!"})
        else:
            return JsonResponse({'status': 'You need to login first!'})
    return redirect('/')  # if someone try to access without POST method it will redirect to the homer page




# Delete Wishlist Item
def delete_wishlist_item(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            prod_id = int(request.POST.get('product_id'))

            wishlist_item = Wishlist.objects.filter(
                user=request.user,
                product_id=prod_id
            ).first()

            if wishlist_item:
                wishlist_item.delete()
                return JsonResponse({'status': 'Product removed from wishlist!'})
            else:
                return JsonResponse({'status': 'Product not found in wishlist!'})

        else:
            return JsonResponse({'status': 'You need to login first!'})

    return redirect('/')