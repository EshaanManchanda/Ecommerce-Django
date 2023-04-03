from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ObjectDoesNotExist
from .forms import CreateUserForm, OrderForm, ProductForm
from django.contrib import messages
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from .models import company as Company, Item as Product, category as Category, Order
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, View
from .decorators import unauthenticated_user, allowed_users


@login_required(login_url='shop:account_login')
@allowed_users(allowed_roles=['shop'])
def index(request):
    product = Product.objects.all()
    product_count = product.count()
    order = Order.objects.all()
    order_count = order.count()
    customer = User.objects.filter(groups=2)
    customer_count = customer.count()

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.customer = request.user
            obj.save()
            return redirect('shop:dashboard-index')
    else:
        form = OrderForm()
    context = {
        'form': form,
        'order': order,
        'product': product,
        'product_count': product_count,
        'order_count': order_count,
        'customer_count': customer_count,
    }
    return render(request, 'shop/dashboard/index.html', context)


@login_required(login_url='user-login')
def products(request):
    product = Product.objects.all()
    product_count = product.count()
    customer = User.objects.filter(groups=1)
    company = Company.objects.get(user=request.user)
    customer_count = customer.count()
    order = Order.objects.all()
    order_count = order.count()
    item = Product()
    product_quantity = Product.objects.filter(title='')
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            product_name = form.cleaned_data.get('title')
            messages.success(request, f'{product_name} has been added')
            return redirect('shop:dashboard-products')
    else:
        form = ProductForm()
    context = {
        'product': product,
        'form': form,
        'company': company,
        'customer_count': customer_count,
        'product_count': product_count,
        'order_count': order_count,
    }
    return render(request, 'shop/dashboard/products.html', context)


@login_required(login_url='user-login')
def product_detail(request, pk):
    item = Product.objects.get(id=pk)
    context = {
        'item': item
    }
    return render(request, 'shop/dashboard/products_detail.html', context)


@login_required(login_url='user-login')
@allowed_users(allowed_roles=['shop'])
def customers(request):
    customer = User.objects.filter(groups=2)
    customer_count = customer.count()
    product = Product.objects.all()
    product_count = product.count()
    order = Order.objects.all()
    order_count = order.count()
    context = {
        'customer': customer,
        'customer_count': customer_count,
        'product_count': product_count,
        'order_count': order_count,
    }
    return render(request, 'shop/dashboard/customers.html', context)


@login_required(login_url='user-login')
@allowed_users(allowed_roles=['shop'])
def customer_detail(request, pk):
    customer = User.objects.filter(groups=2)
    customer_count = customer.count()
    product = Product.objects.all()
    product_count = product.count()
    order = Order.objects.all()
    order_count = order.count()
    customers = User.objects.get(id=pk)
    context = {
        'customers': customers,
        'customer_count': customer_count,
        'product_count': product_count,
        'order_count': order_count,

    }
    return render(request, 'dashboard/customers_detail.html', context)


@login_required(login_url='user-login')
@allowed_users(allowed_roles=['shop'])
def product_edit(request, pk):
    item = Product.objects.get(id=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('shop:dashboard-products')
    else:
        form = ProductForm(instance=item)
    context = {
        'form': form,
    }
    return render(request, 'shop/dashboard/products_edit.html', context)


@login_required(login_url='user-login')
@allowed_users(allowed_roles=['shop'])
def product_delete(request, pk):
    item = Product.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('shop:dashboard-products')
    context = {
        'item': item
    }
    return render(request, 'shop/dashboard/products_delete.html', context)

class ItemDetailView(DetailView):
    model = Order
    template_name = "shop/dashboard/order_view.html"
    
class OrderView(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        try:
            order = Order.objects.all()
            print(order)

            context = {
                'object': order
            }
            return render(self.request, 'shop/dashboard/order.html', context)
        except ObjectDoesNotExist:
            messages.warning(self.request, "you do not have any active order")
            return redirect("/")


@login_required(login_url='shop:account_login')
@allowed_users(allowed_roles=['shop'])
def employee(request):
    return render(request, 'shop/dashboard/employee.html')


@unauthenticated_user
def registerPage(request):
    form = CreateUserForm
    company = Company()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='shop')
            user.groups.add(group)
            user.is_staff = True
            user.is_superuser = True
            user.save()
            company.name = form.cleaned_data.get(
                'company_name')
            company.user = user
            company.save()

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
