# Generated by Django 5.1.3 on 2025-03-13 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0005_wishlist_quantity_wishlist_size_wishlist_weight'),
    ]

    operations = [
        migrations.AddField(
            model_name='productbookings',
            name='status',
            field=models.CharField(default='pending', max_length=100),
        ),
    ]
