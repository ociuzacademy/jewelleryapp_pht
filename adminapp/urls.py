from django.urls import path
from . import views 
from adminapp.views import *
urlpatterns = [
    path('admin_index/', views.admin_index, name='admin_index'), 
    path('',views.admin_login,name='admin_login'),
    path("logout/", views.admin_logout, name="admin_logout"),
    path('add/', add_category, name='add_category'),
    path('list/', category_list, name='category_list'),
    path('edit/<int:category_id>/', edit_category, name='edit_category'),
    path('delete/<int:category_id>/', delete_category, name='delete_category'),
    path('products/add/', add_product, name='add_product'),
    path('products/', product_list, name='product_list'),
    path('products/edit/<int:product_id>/', edit_product, name='edit_product'),
    path('products/delete/<int:product_id>/', delete_product, name='delete_product'),
]
