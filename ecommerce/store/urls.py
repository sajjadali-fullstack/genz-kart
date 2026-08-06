from django.urls import path
from store import views
from store.controller import auth_views, cart, wishlist, checkout  # For login / logout / Add to cart


urlpatterns = [
    path('', views.home_view, name='home'),
    path('collections/', views.collections_view, name='collections'),

    # Category level: mysite.com/collections/goats/
    path('collections/<str:slug>', views.category_view, name="collectionsView"),

    # Product level: mysite.com/collections/goats/totapari-bakra/
    path('collections/<str:cate_slug>/<str:prod_slug>', views.product_details_view, name="product_details"),

    # For: registration / login / logout
    path('register/', auth_views.register_view, name='register'),
    path('login/', auth_views.login_page_view, name='login'),
    path('logout/', auth_views.logout_page_view, name='logout'),

    # Cart
    path('add-to-cart/', cart.add_to_cart_view, name='add_to_cart'),
    path('cart/', cart.view_cart, name='view_cart'),
    path('update-cart/', cart.update_cart_view, name='update_cart'),
    path('delete-cart-item/', cart.delete_cart_item, name='delete_cart_item'),

    path('wishlist/', wishlist.index, name='wishlist'),  # inside wishlist.py index function 
    path('add-to-wishlist/', wishlist.add_to_wishlist, name='add_to_wishlist'),
    path('delete-wishlist-item/', wishlist.delete_wishlist_item, name='delete_wishlist_item'),

    path('checkout/', checkout.index, name='checkout')

]
