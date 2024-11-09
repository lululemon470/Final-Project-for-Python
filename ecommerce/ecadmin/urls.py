"""
URL configuration for ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "ecadmin"

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('slideshow/', views.slideshow, name='slideshow'),


    path('products/', views.product_list, name='product-list'),
    path('products/post', views.product_post, name='product-post'),
    path('products/update/<str:pk>/', views.product_update, name='product-update'),
    path('products/delete/<str:pk>/', views.product_delete, name='product-delete'),

    # Category
    path('category/', views.category_list, name='category-list'),
    path('category/post', views.category_post, name='category-post'),
    path('category/update/<str:pk>', views.category_update, name='category-update'),
    path('category/delete/<str:pk>', views.category_delete, name='category-delete'),

    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
]