from django.shortcuts import render

# Create your views here.
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .models import TblRegister
from .serializers import RegisterSerializer
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .models import TblRegister
from .serializers import RegisterSerializer

class RegisterViewSet(viewsets.ModelViewSet):
    queryset = TblRegister.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]
    http_method_names = ["post"]  # Corrected from 'http_method' to 'http_method_names'

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"message": "User registered successfully", "user_id": user.id, "role": "user"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from .models import TblRegister
from .serializers import RegisterSerializer

class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        if not email or not password:
            return Response({"error": "Email and password are required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = TblRegister.objects.get(email=email, password=password)
            return Response({
                "message": "Login successful",
                "user_id": user.id,
                "name": user.name,
                "status": user.status
            }, status=status.HTTP_200_OK)
        except TblRegister.DoesNotExist:
            return Response({"error": "Invalid email or password"}, status=status.HTTP_401_UNAUTHORIZED)


from rest_framework import viewsets
from adminapp.models import Category
from .serializers import CategorySerializer
from rest_framework.permissions import AllowAny

class CategoryViewSet(viewsets.ReadOnlyModelViewSet):  # ReadOnlyModelViewSet allows only GET methods
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]  # Allows anyone to view categories


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from adminapp.models import Category
from .serializers import CategorySerializer

class CategoryByNameView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, name):
        try:
            category = Category.objects.get(name__iexact=name)  # Case-insensitive lookup
            serializer = CategorySerializer(category)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Category.DoesNotExist:
            return Response({"error": "Category not found"}, status=status.HTTP_404_NOT_FOUND)



from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from adminapp.models import Category, Product
from .serializers import ProductSerializer

class ProductByCategoryView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, category_name):
        normalized_name = category_name.strip()  # Remove extra spaces
        try:
            category = Category.objects.get(name__iexact=normalized_name)  # Case-insensitive lookup
            products = Product.objects.filter(category=category)  # Get products in this category
            serializer = ProductSerializer(products, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Category.DoesNotExist:
            return Response({"error": "Category not found"}, status=status.HTTP_404_NOT_FOUND)
