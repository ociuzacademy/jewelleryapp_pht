from rest_framework import serializers
from .models import TblRegister

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = TblRegister
        fields = ["id", "name", "email", "password", "phone_number", "address", "profile", "status"]  # Added status field

    def create(self, validated_data):
        return TblRegister.objects.create(**validated_data)


from rest_framework import serializers
from adminapp.models import Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name", "picture", "description"]



from rest_framework import serializers
from adminapp.models import Product, ProductImage

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ["id", "image"]  # Include only relevant fields

class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)  # Include product images

    class Meta:
        model = Product
        fields = ["id", "name", "description", "size", "stock", "gram", "price", "images"]
