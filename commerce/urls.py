from django.urls import path
from . import  views

urlpatterns = [
    path('products/', views.ProductsView.as_view(), name='products'),
    path('featured-products/', views.FeaturedProductsView.as_view(), name='featured-products'),
    path('categories/', views.CategorysView.as_view(), name='categories'),
    path('cart-items/', views.CartItemsView.as_view(), name='cart-items'),
    path('cart-items/<int:pk>/', views.CartItemView.as_view(), name='cart-items'),
    path('add-to-cart/<int:product_id>/', views.AddToCartView.as_view(), name='add-to-cart'),
]
