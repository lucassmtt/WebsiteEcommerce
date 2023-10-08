from rest_framework import serializers
from api.models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'name',
            'description'
        ]


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fiels = [
            'name',
            'price',
            'description',
            'lenght',
            'category_oid'
        ]

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fiels = [
            'name',
            'email',
            'phone',
            'cpf',
        ]
        
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fiels = [
            'user_oid',
            'totalPrice',
            'status'
        ]

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fiels = [
            'order_oid',
            'product_oid',
            'quantity'
        ]
