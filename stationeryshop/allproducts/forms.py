from django import forms
from .models import productsdetails

class products(forms.ModelForm):
    class Meta:
        model = productsdetails
        fields = ['name', 'price', 'color', 'image', 'quantity', 'category']