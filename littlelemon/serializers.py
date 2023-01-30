from rest_framework import serializers
from .models import MenuItem, Category

from decimal import Decimal


class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug']


class MenuItemSerializer(serializers.ModelSerializer):
    after_tax = serializers.SerializerMethodField(method_name='price_after_tax')
    category = serializers.HyperlinkedIdentityField('category-detail')

    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'inventory', 'category', 'price', 'after_tax']
        extra_kwargs = {
            'price': {'min_value': 2},
            'inventory': {'min_value': 0}
        }
 
    def price_after_tax(self, product:MenuItem):
        return round(product.price * Decimal(1.1), 2)