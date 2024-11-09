from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from shop.models import Product, Category  # Absolute import # Importing from another app
from .forms import ProductForm, CategoryForm


def category_list(request):
    category = Category.objects.all()
    return render(request, 'ecadmin/category/category.html', {'categories': category})

def category_delete(request, pk):
    category = Category.objects.get(id=pk)
    if request.method == "POST":
        category.delete()
        return redirect('ecadmin:category-list')
    context = {'item': category}
    return render(request, 'ecadmin/category/delete.html', context)

def category_update(request, pk):
    category = Category.objects.get(id=pk)
    form = CategoryForm(instance=category)

    if request.method == "POST":
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('ecadmin:category-list')
    context = {'form': form, 'item': category}
    return render(request, 'ecadmin/category/update.html', context)

def category_post(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.user = request.user
            category.save()
            return redirect('ecadmin:category-list')
    form = CategoryForm()
    return render(request, 'ecadmin/category/add.html', {'form': form})

def product_delete(request, pk):
    products = Product.objects.get(id=pk)
    if request.method == "POST":
        products.delete()
        return redirect('ecadmin:product-list')
    context = {'item': products}
    return render(request, 'ecadmin/product/delete.html', context)

def product_update(request, pk):
    products = Product.objects.get(id=pk)
    form = ProductForm(instance=products)

    if request.method == "POST":
        form = ProductForm(request.POST , request.FILES, instance=products)
        if form.is_valid():
            form.save()
            return redirect('ecadmin:product-list')
    context = {'form': form, 'item': products}
    return render(request, 'ecadmin/product/update.html', context)


def product_post(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)  # Include request.FILES for file data
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            return redirect('ecadmin:product-list')
    form = ProductForm()
    return render(request, 'ecadmin/product/add.html', {'form': form})

def product_list(request):
    products = Product.objects.all()  # Fetching all Product data
    return render(request, 'ecadmin/product/product.html', {'products': products})

@login_required(login_url='ecadmin:login')
def home(request):
    return render(request, "ecadmin/home.html")

@login_required(login_url='ecadmin:login')
def slideshow(request):
    return render(request, "ecadmin/slideshow.html")

@login_required(login_url='ecadmin:login')
def product(request):
    return render(request, "ecadmin/product/product.html")

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('ecadmin:home')  # Redirect after login
        else:
            messages.error(request, 'Invalid credentials')
    return render(request, 'ecadmin/pages-sign-in.html')  # Render your login template


def logout_view(request):
    logout(request)
    return redirect('ecadmin:home')  # Redirect after logout


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('ecadmin:login')
        else:
            print(form.errors)  # Add this line to see the form validation errors
    else:
        form = UserCreationForm()

    return render(request, 'ecadmin/pages-sign-up.html', {'form': form})


