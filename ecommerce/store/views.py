from django.shortcuts import render


# Create your Business logic / views here 👇.

# 1. Home View
def home_view(request):
    return render(request, 'store/index.html')
    