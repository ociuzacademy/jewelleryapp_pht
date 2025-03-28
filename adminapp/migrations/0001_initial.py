# Generated by Django 5.1.3 on 2025-03-11 07:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('subcategories', models.JSONField(default=list)),
                ('icon', models.ImageField(blank=True, null=True, upload_to='category_icons/')),
            ],
        ),
        migrations.CreateModel(
            name='tbl_admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Tblemployee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=128)),
                ('phone', models.CharField(blank=True, max_length=15, null=True)),
                ('position', models.CharField(blank=True, max_length=100)),
                ('address', models.CharField(blank=True, max_length=200)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='employee_image/')),
                ('date_joined', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subcategory', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('stock', models.PositiveIntegerField()),
                ('main_image', models.ImageField(upload_to='product_images/')),
                ('images', models.JSONField(default=list)),
                ('sizes', models.JSONField(default=list)),
                ('weights', models.JSONField(default=list)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='adminapp.category')),
            ],
        ),
    ]
