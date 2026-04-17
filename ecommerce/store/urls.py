from django.urls import path
from store import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('collections/', views.collections_view, name='collections'),

    # Category level: mysite.com/collections/goats/
    path('collections/<str:slug>', views.category_view, name="collectionsView"),

    # Product level: mysite.com/collections/goats/totapari-bakra/
    path('collections/<str:cate_slug>/<str:prod_slug>', views.product_details_view, name="product_details"),
]
