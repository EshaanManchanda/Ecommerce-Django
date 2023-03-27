
app_name = 'shop'
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index, name='shop-index'),
    path('employee/', views.employee, name='shop-employee'),
    path('product/', views.product, name='shop-product'),
    path('order/', views.order, name='shop-order'),
    path('login/', views.loginPage, name='account_login'),
    path('signup/', views.registerPage, name='account_signup'),
    path('logout/', views.logoutUser, name='account_logout'),
]