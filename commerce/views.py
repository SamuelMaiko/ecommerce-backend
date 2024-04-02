from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product, Category, CartItem
from accounts.models import CustomUser
from .serializers import ProductSerializer, CategorySerializer, CartItemSerializer
from django.db.models import Q
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication, SessionAuthentication

# Create your views here.
@method_decorator(csrf_exempt, name='dispatch')
class ProductsView(APIView):
    def get(self, request):
        products=Product.objects.all()
        serializer= ProductSerializer(products, many=True)
        response_dict=dict(products=serializer.data)
        return Response(response_dict, status=status.HTTP_200_OK)

class FeaturedProductsView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    def get(self, request):
        products=Product.objects.filter(Q(is_featured=True))
        serializer= ProductSerializer(products, many=True)
        response_dict=dict(products=serializer.data)
        return Response(response_dict, status=status.HTTP_200_OK)

class CategorysView(APIView):
    def get(self, request):
        all_categories=Category.objects.all()
        serializer= CategorySerializer(all_categories, many=True)
        response_dict=dict(categories=serializer.data)
        return Response(response_dict, status=status.HTTP_200_OK)

class CartItemsView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    def get(self, request):
        user=request.user
        cart_items=CartItem.objects.filter(Q(cart=user.cart))
        serializer= CartItemSerializer(cart_items, many=True)
        response_dict=dict(cart_items=serializer.data, cart_total=user.cart.total)
        return Response(response_dict, status=status.HTTP_200_OK)

class CartItemView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    def patch(self, request, pk):
        user=request.user
        try:
            # see if belongs to the user
            cart_item = CartItem.objects.get(pk=pk)
        except CartItem.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = CartItemSerializer(cart_item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save(quantity=serializer.validated_data['quantity'])
            response_dict=dict(serializer_data=serializer.data, cart_total=user.cart.total)
            return Response(response_dict, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):
        try:
            # see if belongs to the user
            cart_item = CartItem.objects.get(pk=pk)
        except CartItem.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        cart_item.delete()
        response_dict=dict(message="Removed from cart successfully")
        return Response(response_dict, status=status.HTTP_200_OK)
        
class AddToCartView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    def post(self, request, product_id):
        user=request.user
        quantity=request.data.get("quantity")
        product=Product.objects.get(pk=product_id)
        CartItem.objects.create(cart=user.cart, product=product, quantity=quantity)
        response_dict=dict(message="Product added to cart successfully")
        return Response(response_dict, status=status.HTTP_200_OK)
        
        