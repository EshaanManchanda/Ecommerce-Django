
app_name = 'emp'
from django.contrib import admin
from django.urls import path,include
from .views import EmpView

urlpatterns = [
    path('', EmpView, name='EmpV'),
]