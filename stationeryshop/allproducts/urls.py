from django.urls import path
from . import views

urlpatterns = [
    path('', views.productsdata, name='all_products'),
    path('notebooks/', views.notebooks, name='notebooks'),
    path('new/', views.add_new_product, name='add_new_product'),
    path('<int:id>/edit/', views.update_product, name='update_product'),
    path('<int:id>/delete/', views.delete_product, name='delete_product'),
]