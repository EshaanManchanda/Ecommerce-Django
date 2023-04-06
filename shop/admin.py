from django.contrib import admin

from .models import Item,company,Coupon,comments,category,OrderItem,Order,Address,Payment,subcategory,AboutUs
# Register your models here.
admin.site.register(Item)
admin.site.register(AboutUs)
admin.site.register(comments)
admin.site.register(company)
admin.site.register(Coupon)
admin.site.register(category)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Address)
admin.site.register(Payment)
admin.site.register(subcategory)
