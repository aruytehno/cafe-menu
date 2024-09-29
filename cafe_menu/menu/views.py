from django.shortcuts import render

from .models import Product


def home(request):
    return render(request, 'home.html')


def menu(request):
    products = Product.objects.filter(item_in_stock='True').order_by("item_category", "item_name")
    list_categories = []
    for product in products:
        list_categories.append(product.item_category)
    list_categories = [i for n, i in enumerate(list_categories) if i not in list_categories[:n]]
    data = {"products": products, "categories": list_categories}
    return render(request, 'menu.html', context=data)
