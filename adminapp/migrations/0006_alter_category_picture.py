# Generated by Django 5.1.3 on 2025-02-26 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0005_delete_subcategory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='category_pictures/'),
        ),
    ]
