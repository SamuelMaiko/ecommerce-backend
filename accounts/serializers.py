from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import CustomUser, Supplier
from commerce.serializers import ProductSerializer

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=10, write_only=True, required=True)
    first_name = serializers.CharField(max_length=15, required=True)
    last_name = serializers.CharField(max_length=15, required=False)
    email = serializers.EmailField(max_length=15, required=True)

    def create(self, validated_data):
        user=CustomUser.objects.create_user(**validated_data)
        return user
    class Meta: 
        model = CustomUser
        fields = ['email', 'password', "first_name", "last_name"]
        extra_kwargs = {
            'password': {'write_only': True}
        }
        
class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['phone_number','username', 'email', 'first_name', 'last_name']
        
class SupplierSerializer(serializers.ModelSerializer):
    products=ProductSerializer(many=True)
    class Meta:
        model = Supplier
        fields = ['id','name','email','phone_number','image', 'address', 'is_popular', 'products']
        
