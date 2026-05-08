from django.shortcuts import render, redirect
from store.forms import CustomUserForm
from django.contrib import messages

# Create your Login, Logout / views here 👇.

def register_view(request):
    form = CustomUserForm()
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registered Successfully! Login to Continue")
            return redirect('/login')

    context = {'form':form}
    return render(request, 'store/auth/register.html', context)

def login_page_view(request):
    return render(request, 'store/auth/login.html')