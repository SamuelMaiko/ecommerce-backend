from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db.models import Sum, F
from datetime import timedelta, date, datetime
from decimal import Decimal
from django.conf import settings
from .managers import CustomUserManager

# Create your models here.

class CustomUser(AbstractUser, PermissionsMixin):
    username = models.CharField(max_length=15, unique=True, blank=True, null=True)
    email = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    USERNAME_FIELD = 'email'
    # EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()
    class Meta:
        db_table="users"

    def __str__(self):
        return self.email
CustomUser._meta.get_field('groups').remote_field.related_name = 'customuser_groups'
CustomUser._meta.get_field('user_permissions').remote_field.related_name = 'customuser_permissions'

class UserProfile(models.Model):
    user=models.ForeignKey(CustomUser,  on_delete=models.CASCADE, related_name="profile")
    phone_number = models.CharField(max_length=10, unique=True, blank=True, null=True)
    image=models.ImageField(upload_to='profiles/', default='profiles/default.jpg')
    
    def __str__(self):
        return f"{self.user.email}'s profile"
    
    class Meta:
        db_table = 'user_profiles'
        

class Supplier(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    image=models.ImageField(upload_to='suppliers/', null=True, blank=True)
    address = models.TextField()
    is_popular=models.BooleanField(default=False)

    def __str__(self):
        return self.name
        
    
