from rest_framework import serializers
from .models import MenuItem, Category

from decimal import Decimal


class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = ['id', 'title', 'slug']


class MenuItemSerializer(serializers.HyperlinkedModelSerializer):
    after_tax = serializers.SerializerMethodField(method_name='price_after_tax')

    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'inventory', 'category', 'price', 'after_tax']
 
    def price_after_tax(self, product:MenuItem):
        return round(product.price * Decimal(1.1), 2)