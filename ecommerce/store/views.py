from django.shortcuts import render, redirect
from store.models import Category, Product

# Create your Business logic / views here 👇.

# 1. Home View
def home_view(request):
    return render(request, 'store/index.html')

def collections_view(request):
    category = Category.objects.filter(status=0)
    context = {'category': category}
    return render(request, "store/products/collections.html", context)
