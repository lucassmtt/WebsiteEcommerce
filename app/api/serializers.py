from rest_framework import serializers
from api.models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['__all__']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fiels = ['__all__']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fiels = ['__all__']
        
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fiels = ['__all__']

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fiels = ['__all__']
