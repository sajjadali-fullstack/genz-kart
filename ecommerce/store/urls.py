from django.urls import path
from store import views

urlpatterns = [
    path('home/', views.home_view, name='home'),
]