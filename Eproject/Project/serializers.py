from rest_framework import serializers
from .models import Order_item, Order,  Product, Product_Category, Shipping
from django.contrib.auth.models import User



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class Order_itemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order_item
        fields= '__all__'
          


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields= '__all__'

class Product_CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Product_Category
        fields= '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields= '__all__'

class ShippingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipping
        fields= '__all__'
