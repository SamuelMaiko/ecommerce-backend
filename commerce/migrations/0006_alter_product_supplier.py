# Generated by Django 5.0.2 on 2024-03-26 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_supplier_image_supplier_is_popular'),
        ('commerce', '0005_product_supplier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='supplier',
            field=models.ManyToManyField(blank=True, null=True, related_name='products', to='accounts.supplier'),
        ),
    ]
