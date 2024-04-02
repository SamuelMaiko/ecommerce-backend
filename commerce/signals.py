from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import CartItem

@receiver(post_save, sender=CartItem)
def update_cart_total(sender, instance, created, **kwargs):
    cart_items=instance.cart.cart_items.all()
    total=0
    for cart_item in cart_items:
        total+=cart_item.total_price
    
    instance.cart.total=total
    instance.cart.save()

@receiver(post_delete, sender=CartItem)
def update_cart_total(sender, instance, **kwargs):
    cart_items=instance.cart.cart_items.all()
    total=0
    for cart_item in cart_items:
        total+=cart_item.total_price
    
    instance.cart.total=total
    instance.cart.save()
    