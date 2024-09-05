from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'shop/dashboard/index.html')


def employee(request):
    return render(request, 'shop/dashboard/employee.html')


def product(request):
    return render(request, 'shop/dashboard/product.html')


def order(request):
    return render(request, 'shop/dashboard/order.html')
