from rest_framework import serializers
from .models import Product, Category, CartItem

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=['id', 'name','description','image', 'price', 'discount', 'is_featured', 'is_discounted', 'new_price']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=['id', 'name','description', 'image']

class CartItemSerializer(serializers.ModelSerializer):
    product=ProductSerializer()
    class Meta:
        model=CartItem
        fields=['id', 'product', 'quantity']