# Generated by Django 5.1.3 on 2025-02-27 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tblregister',
            name='status',
            field=models.CharField(choices=[('approved', 'Approved'), ('blocked', 'Blocked')], default='approved', max_length=10),
        ),
    ]
