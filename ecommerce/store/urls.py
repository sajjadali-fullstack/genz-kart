from django.urls import path
from store import views

urlpatterns = [
    path('home/', views.home_view, name='home'),
    # Category level: mysite.com/collections/goats/
    # path('collections/<str:cate_slug>', views.view_category, name="view_category"),

    # Product level: mysite.com/collections/goats/totapari-bakra/
    # path('collections/<str:cate_slug>/<str:prod_slug>', views.product_details, name="product_details"),
]
