from django.shortcuts import render

from products.models import ProductCategory, Product
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.cache import cache
from django.conf import settings
from django.views.decorators.cache import cache_page, never_cache


# def get_links_menu(category_id=None):
#     if settings.LOW_CACHE:
#        key = 'categories'
#         categories = cache.get(key)
#         if categories is None:
#             categories = Product.objects.filter(category_id=category_id)
#             cache.set(key, categories)
#         return categories
#     else:
#         return Product.objects.filter(category_id=category_id)


@never_cache
def index(request):
    context = {'title': 'GeekShop'}
    return render(request, 'products/index.html', context)


@cache_page(3600)
def products(request, category_id=None, page=1):
    if category_id:
        products = Product.objects.filter(category_id=category_id)
    else:
        products = Product.objects.all()
    paginator = Paginator(products, 3)
    try:
        products_paginator = paginator.page(page)
    except PageNotAnInteger:
        products_paginator = paginator.page(1)
    except EmptyPage:
        products_paginator = paginator.page(paginator.num_pages)
    context = {
        'title': 'GeekShop - Продукты',
        'categories': ProductCategory.objects.all(),
        'products': products_paginator,
    }
    return render(request, 'products/products.html', context)