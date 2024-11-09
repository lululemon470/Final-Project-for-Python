from django import forms
from shop.models import Product, Category

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ("user", )

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        exclude = ("user", )
