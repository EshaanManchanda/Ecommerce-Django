
app_name = 'user'
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.HomeView, name="home"),
    path('register/',views.registerPage, name="register"),
    path('login/',views.loginPage, name="login"),
    path('logout/',views.logoutUser, name="logout"),
    path('products/',views.products, name="products"),
    path('customer/',views.customer, name="customer"),
    path('category/',views.category, name="category"),
    path('subcategory/',views.subcategory, name="subcategory"),
    path('order-summary/', views.OrderSummaryView.as_view(), name='order-summary'),
]