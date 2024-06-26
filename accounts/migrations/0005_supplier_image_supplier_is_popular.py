# Generated by Django 5.0.2 on 2024-03-24 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_supplier'),
    ]

    operations = [
        migrations.AddField(
            model_name='supplier',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='suppliers/'),
        ),
        migrations.AddField(
            model_name='supplier',
            name='is_popular',
            field=models.BooleanField(default=False),
        ),
    ]
