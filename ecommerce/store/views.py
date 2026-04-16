from django.shortcuts import render, redirect
from store.models import Category, Product
from django.contrib import messages 
# Create your Business logic / views here 👇.

# 1. Home View
def home_view(request):
    return render(request, 'store/index.html')

# collections
def collections_view(request):
    category = Category.objects.filter(status=0)
    context = {'category': category}
    return render(request, "store/products/collections.html", context)


# collecrtionView
def category_view(request, slug):
    if(Category.objects.filter(slug=slug, status=0)):
        products = Product.objects.filter(category__slug=slug)
        category_name = Category.objects.filter(slug=slug).first()
        context = {'products':products, 'category_name':category_name}
        return render(request, 'store/products/index.html', context)
    else:
        messages.warning(request, "No Such Category Found")
        return redirect('collections')