from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='shop-index'),
    path('employee/', views.employee, name='shop-employee'),
    path('product/', views.product, name='shop-product'),
    path('order/', views.order, name='shop-order'),
]
