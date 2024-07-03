from django.shortcuts import render

def all_stationery_products(request):
    return render(request, 'index.html')
