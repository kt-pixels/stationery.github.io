from django.shortcuts import render, redirect, get_object_or_404
from .models import productsdetails
from .forms import products
from django.http import JsonResponse

# Create your views here.

def notebooks(request):
    return render(request, 'allproducts/notebooks.html')

# def productsdata(request):
#     data = productsdetails.objects.all()
#     return render(request, 'allproducts/allProducts.html', {'data': data})

def productsdata(request):
    notebook = productsdetails.objects.filter(category='NoteBooks')
    pens = productsdetails.objects.filter(category= 'Pens')
    Pencils = productsdetails.objects.filter(category= 'Pencils')
    Dairy = productsdetails.objects.filter(category= 'Dairy')
    Tape = productsdetails.objects.filter(category= 'Tape')
    Sheets = productsdetails.objects.filter(category= 'Sheets')

    context = {
        'notebooks': notebook,
        'pens': pens,
        'pencils': Pencils,
        'dairy': Dairy,
        'tape': Tape,
        'sheets': Sheets,
    }

    return render(request, 'allproducts/allProducts.html', context)

def add_new_product(request):
    if request.method == 'POST':
        form = products(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('all_products')
    else:
        form = products()
    return render(request, 'allproducts/products_form.html', {'form': form})

def update_product(request, id):
    product = get_object_or_404(productsdetails, id = id)
    if request.method == 'POST':
        form = products(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('all_products')
    else:
        form = products(instance=product)
    return render(request, 'allproducts/products_form.html', {'form': form})

def delete_product(request, id):
    product = get_object_or_404(productsdetails, id = id)
    if request.method == 'POST':
        product.delete()
        return redirect('all_products')
    return render(request, 'allproducts/product_confirm_delete.html', {'product': product})

