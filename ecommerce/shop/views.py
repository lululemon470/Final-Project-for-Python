from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Product, Category

def home(request):
    context = {"slider": True, "aside": True}
    return render(request, "shop/home.html", context)

def contact(request):
    context = {"slider": False}
    return render(request, "shop/contact-us.html", context)

def shop(request):
    products = Product.objects.all()
    category = Category.objects.all()# Fetching all Product data# Fetch all products or filter as needed
    paginator = Paginator(products, 9)  # Show 9 products per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "shop/shop.html", {'page_obj': page_obj, 'category': category})

def shop_category(request, category_name):
    category = get_object_or_404(Category, category_name=category_name)
    # Filter products based on the retrieved category
    products = Product.objects.filter(category=category)
    category = Category.objects.all()
    paginator = Paginator(products, 9)  # Show 9 products per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "shop/shop.html", {'page_obj': page_obj, 'category': category})