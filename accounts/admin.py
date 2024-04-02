from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import CustomUser, UserProfile, Supplier


# Register your models here.
class CustomUserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ('email','first_name','last_name', 'username','is_active', 'is_staff', 'is_superuser')  # Display phone number in the user list
    fieldsets = (
        (None, {'fields': ('password','email','first_name','last_name',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Important dates', {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(UserProfile)
admin.site.register(Supplier)
