from django.http import JsonResponse
from store.models import Product


def search_products(request):

    if request.method == "GET":

        search = request.GET.get("search", "")

        products = Product.objects.filter(
            name__icontains=search
        )[:10]

        data = []

        for product in products:
           data.append({
    "id": product.id,
    "name": product.name,
    "category_slug": product.category.slug,
    "product_slug": product.slug,
})
        return JsonResponse(data, safe=False)

    return JsonResponse([], safe=False)