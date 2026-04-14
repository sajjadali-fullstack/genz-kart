from django.shortcuts import render


# Create your Business logic / views here 👇.

# 1. Home View
def home_view(request):
    return render(request, 'store/index.html')

# def view_category(request, cate_slug):
#     if (Category.objects.filter(slug=cate_slug, status=0)):
#         products = Product.objects.filter(category__slug=cate_slug)
#         category_name = Category.objects.filter(slug=cate_slug).first()
#         context = {'products': products, 'category_name': category_name}
#         return render(request, "store/products/index.html", context)
#     else:
#         return redirect('home')

# # Single product (Totapari Bakra) ki details dikhane ke liye
# def product_details(request, cate_slug, prod_slug):
#     if (Category.objects.filter(slug=cate_slug, status=0)):
#         if (Product.objects.filter(slug=prod_slug, status=0)):
#             products = Product.objects.filter(slug=prod_slug, status=0).first()
#             context = {'products': products}
#             return render(request, "store/products/view.html", context)
#         else:
#             return redirect('home')
#     else:
#         return redirect('home')