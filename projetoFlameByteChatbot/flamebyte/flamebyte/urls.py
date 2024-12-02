from django.urls import path
from products.views import home, products_list, product_detail, register, login_view, logout_view

urlpatterns = [
    path('', home, name='home'),
    path('products/', products_list, name='products_list'),
    path('products/<int:product_id>/', product_detail, name='product_detail'),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]