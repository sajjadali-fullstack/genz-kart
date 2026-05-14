from django.shortcuts import render, redirect
from store.forms import CustomUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout  # for login

# Create your Login, Logout / views here 👇.

# For Registration
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

# For Login 
def login_page_view(request):

    if request.user.is_authenticated:  # If u r login try to do --> http://localhost:8000/login/ so hey will not accept 
        messages.warning(request, "You are already loged in!")
        return redirect("/") 
    else:

        if request.method == 'POST':
            name = request.POST.get('username')  # login.html --> name="username"
            pwd = request.POST.get('password') # login.html --> name="password"

            user = authenticate(request, username=name, password=pwd)

            if user is not None:
                login(request, user)
                messages.success(request, "Loged In Sucessfully!")
                return redirect('/')
            
            else:
                messages.error(request, "Invalid Username or Passwoprd")
                return redirect('/login')


        return render(request, 'store/auth/login.html')


# For Logout
def logout_page_view(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, "Logged out Sucessfully!")
        return redirect('/')
