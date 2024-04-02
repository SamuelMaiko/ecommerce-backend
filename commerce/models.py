from django.db import models
from django.conf import settings
from accounts.models import Supplier

# Create your models here.
class Cart(models.Model):
    user=models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='cart')
    products=models.ManyToManyField('Product', related_name='carts')
    total=models.DecimalField(max_digits=10, decimal_places=2, default=0)
    
    
    @property
    def product_count(self):
        return len(self.products)
    
    def __str__(self):
        return f"{self.user.email}'s cart"
    
    class Meta:
        db_table = 'carts'
        
class Category(models.Model):
    name=models.CharField(max_length=50)
    description=models.TextField()
    image=models.ImageField(upload_to='categories/')
    
    def __str__(self):
        return self.name
    
    

class Product(models.Model):
    category=models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category', null=True, blank=True)
    supplier=models.ManyToManyField(Supplier, related_name='products', null=True, blank=True)
    name=models.CharField(max_length=50)
    description=models.TextField()
    image=models.ImageField(upload_to='products/', default='products/default.jpg')
    price=models.DecimalField(max_digits=10, decimal_places=2)
    discount=models.DecimalField(max_digits=5, decimal_places=2, default=0)
    is_featured=models.BooleanField(default=False)
    
    @property
    def is_discounted(self):
        return self.new_price<self.price
    
    @property
    def new_price(self):
        if self.discount>0:
            return (1-(self.discount/100))*self.price
        return self.price
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'products'
        
class CartItem(models.Model):
    cart=models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_items')
    product=models.ForeignKey(Product, on_delete=models.CASCADE, related_name='cart_items')
    quantity=models.IntegerField(default=0)
    
    @property
    def total_price(self):
        return self.product.price*self.quantity

    def __str__(self):
        return f"{self.cart.pk} and {self.product.name}'s cart_product"
    
    class Meta:
        db_table = 'cart_items'
        # unique_together=['cart', 'product']