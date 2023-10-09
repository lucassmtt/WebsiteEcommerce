from rest_framework import serializers
from . import models


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = [
            'name',
            'price',
            'description',
            'lenght',
            'category_oid'
        ]