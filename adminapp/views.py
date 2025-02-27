from django.shortcuts import render,redirect,get_object_or_404
# Create your views here.

def admin_index(request):
    if not request.session.get("admin_logged_in"):
        return redirect("admin_login")  # Redirect if not logged in
    
    return render(request, "admin_index.html")

from django.shortcuts import render, redirect
from django.contrib import messages

def admin_logout(request):
    request.session.flush()  # Clear session
    messages.success(request, "You have been logged out.")
    return redirect("admin_login")



from django.shortcuts import render, redirect
from django.contrib import messages
from adminapp.models import tbl_admin  # Import the admin model

def admin_login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        # Check if the email and password match the admin credentials
        if email == "admin@gmail.com" and password == "admin":
            request.session["admin_logged_in"] = True  # Store login session
            messages.success(request, "Login successful!")
            return redirect("admin_index")  # Redirect to admin dashboard

        else:
            messages.error(request, "Invalid email or password. Please try again.")
    
    return render(request, "admin_login.html")  # Render login page


# def admin_login(request):
#     if request.method =='POST':
#         email=request.POST.get('email')
#         password=request.POST.get('password')

#         if email=='admin@gmail.com' and password=='admin':
#             return redirect('admin_index')
#     return render(request,'admin_login.html')






##category##
from django.shortcuts import render, redirect
from .models import Category

def add_category(request):
    if request.method == "POST":
        name = request.POST.get('name')
        description = request.POST.get('description', '')
        picture = request.FILES.get('picture')

        if name and picture:  # Ensuring required fields are provided
            Category.objects.create(name=name, description=description, picture=picture)
            return redirect('category_list')  # Redirect to the list view

    return render(request, 'add_category.html')

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})

def edit_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)

    if request.method == "POST":
        name = request.POST.get('name', category.name)
        description = request.POST.get('description', category.description)
        picture = request.FILES.get('picture')

        category.name = name
        category.description = description

        if picture:  # Only update if a new picture is uploaded
            category.picture = picture

        category.save()
        return redirect('category_list')

    return render(request, 'edit_category.html', {'category': category})

def delete_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    category.delete()
    return redirect('category_list')

from django.shortcuts import render, redirect
from .models import Product, Category

# Add Product View (Without Forms)
from django.shortcuts import render, redirect
from .models import Product, Category, ProductImage
from django.shortcuts import render, redirect
from decimal import Decimal
from .models import Product, ProductImage, Category

def add_product(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        category_id = request.POST.get('category')
        description = request.POST.get('description')
        size = request.POST.get('size')
        stock = request.POST.get('stock')
        gram = request.POST.get('gram')
        price = request.POST.get('price')
        images = request.FILES.getlist('images')  # Get multiple images

        category = Category.objects.get(id=category_id)

        # Create product first
        product = Product.objects.create(
            name=name,
            category=category,
            description=description,
            size=size,
            stock=stock,
            gram=gram,
            price=Decimal(price)
        )

        # Save images associated with the product
        for image in images:
            ProductImage.objects.create(product=product, image=image)

        return redirect('product_list')

    categories = Category.objects.all()
    return render(request, 'add_product.html', {'categories': categories})


from django.shortcuts import render
from .models import Product, Category

def product_list(request):
    search_query = request.GET.get('search', '')
    category_filter = request.GET.get('category', '')

    products = Product.objects.all()
    
    if search_query:
        products = products.filter(name__icontains=search_query)
    
    if category_filter:
        products = products.filter(category_id=category_filter)

    categories = Category.objects.all()
    
    return render(request, 'product_list.html', {'products': products, 'categories': categories})



from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, ProductImage, Category
from decimal import Decimal

def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    categories = Category.objects.all()

    if request.method == 'POST':
        product.name = request.POST.get('name')
        product.category = get_object_or_404(Category, id=request.POST.get('category'))
        product.description = request.POST.get('description')
        product.size = request.POST.get('size')
        product.stock = request.POST.get('stock')
        product.gram = request.POST.get('gram')
        product.price = Decimal(request.POST.get('price'))
        product.save()

        # Handle new images
        images = request.FILES.getlist('images')
        for image in images:
            ProductImage.objects.create(product=product, image=image)

        return redirect('product_list')

    return render(request, 'edit_product.html', {'product': product, 'categories': categories})



def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    product.delete()
    return redirect('product_list')
