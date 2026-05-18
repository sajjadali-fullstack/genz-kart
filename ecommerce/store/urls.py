from django.urls import path
from store import views
from store.controller import auth_views, cart  # For login / logout / Add to cart


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

]
