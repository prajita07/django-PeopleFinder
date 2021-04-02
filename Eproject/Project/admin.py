from django.contrib import admin
from .models import Order, Order_item,  Product, Product_Category, Shipping

# Register your models here.
admin.site.register(Shipping)
admin.site.register(Order)
admin.site.register(Order_item)
admin.site.register(Product_Category)
admin.site.register(Product)
