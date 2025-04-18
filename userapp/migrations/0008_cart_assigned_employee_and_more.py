# Generated by Django 5.1.3 on 2025-03-14 08:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0001_initial'),
        ('userapp', '0007_cartcard_cartupi'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='assigned_employee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assigned_carts', to='adminapp.tblemployee'),
        ),
        migrations.AddField(
            model_name='productbookings',
            name='assigned_employee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assigned_bookings', to='adminapp.tblemployee'),
        ),
    ]
