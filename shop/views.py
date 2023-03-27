from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users

@login_required(login_url='shop:account_login')
@allowed_users(allowed_roles=['shop'])
def index(request):
    return render(request, 'shop/dashboard/index.html')

@login_required(login_url='shop:account_login')
@allowed_users(allowed_roles=['shop'])
def employee(request):
    return render(request, 'shop/dashboard/employee.html')

@login_required(login_url='shop:account_login')
@allowed_users(allowed_roles=['shop'])
def product(request):
    return render(request, 'shop/dashboard/product.html')

@login_required(login_url='shop:account_login')
@allowed_users(allowed_roles=['shop'])
def order(request):
    return render(request, 'shop/dashboard/order.html')

@unauthenticated_user
def registerPage(request):
    form = CreateUserForm
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user=form.save()
            username = form.cleaned_data.get('username')
            group=Group.objects.get(name='shop')
            user.groups.add(group)
            user.is_staff=True
            user.is_superuser=True
            user.save()
            messages.success(request, 'Account was created for ' + username)
            return redirect("shop:account_login")

    context = {'form': form}
    return render(request, 'shop/partials/signup.html', context)

@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('shop:shop-index')
        else:
            messages.info(request, 'username or password is incorrect')

    return render(request, 'shop/partials/login.html')


def logoutUser(request):
    logout(request)
    return redirect('shop:account_login')