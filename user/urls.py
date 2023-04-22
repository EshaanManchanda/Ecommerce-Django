from .views import HomeView, registerPage, loginPage, logoutUser, OrderSummaryView, CatView, CheckoutView, AboutUs, Author, ItemDetailView, add_to_cart, AddCouponView, remove_from_cart, remove_single_item_from_cart, PaymentView, RequestRefundView,subCatView,search, profile,order_history
from django.urls import path, include
from django.contrib import admin
app_name = 'user'

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('register/', registerPage, name="register"),
    path('search/', search, name="search"),
    path('login/', loginPage, name="login"),
    path('logout/', logoutUser, name="logout"),
    path('category/<slug>', CatView.as_view(), name='category'),
    path('subcategory/<slug>', subCatView.as_view(), name='subcategory'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('aboutus/', AboutUs, name='aboutus'),
    path('aboutus/<slug>', Author.as_view(), name='author'),
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('add-coupon/', AddCouponView.as_view(), name='add-coupon'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    path('remove-item-from-cart/<slug>/', remove_single_item_from_cart,
         name='remove-single-item-from-cart'),
    path('payment/<payment_option>/', PaymentView.as_view(), name='payment'),
    path('request-refund/', RequestRefundView.as_view(), name='request-refund'),
    path('profile/<pk>/', profile.as_view(), name='profile'),
    path('order-history/<pk>/', order_history, name='order-history'),
    
]
