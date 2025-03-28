# Generated by Django 5.1.3 on 2025-03-14 15:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0008_cart_assigned_employee_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartcard',
            name='booking',
        ),
        migrations.RemoveField(
            model_name='cartupi',
            name='booking',
        ),
        migrations.AddField(
            model_name='cartcard',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='card_payments', to='userapp.tblregister'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cartupi',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='upi_payments', to='userapp.tblregister'),
            preserve_default=False,
        ),
    ]
