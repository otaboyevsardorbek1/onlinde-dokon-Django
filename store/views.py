import json

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

from store.business_logic.selectors import get_all_category, get_all_products
from store.business_logic.services import Basket
from store.models import  Product


def home_page_view(request):
    context = {
        "category": get_all_category(),
        "products": get_all_products(),
    }
    return render(request, "store/index.html", context=context)


def basket_add(request, slug):
    
    basket = Basket(request)

    current_page = request.META.get("HTTP_REFERER")
    product = Product.objects.get(slug=slug)

    basket.add(product=product)

    return HttpResponseRedirect(current_page)
    

def basket_remove_count(request, slug) -> str:
    
    basket = Basket(request)

    current_page = request.META.get("HTTP_REFERER")
    product = Product.objects.get(slug=slug)

    basket.remove_count(product)

    return HttpResponseRedirect(current_page)

def basket_remove(request, slug):
    
    basket = Basket(request)

    current_page = request.META.get("HTTP_REFERER")
    product = Product.objects.get(slug=slug)

    basket.remove(product)

    return HttpResponseRedirect(current_page)

def cart_page(request):
    basket = Basket(request)
    
    context = {
        'basket': basket
    }

    return render(request, "store/cart.html", context=context)

def shop_page_view(request):

    context = {
        "products": get_all_products(),
    }

    return render(request, "store/shop.html", context=context)



def detail_page(request, slug):
    product = Product.objects.get(slug=slug)
    basket = Basket(request)
    context = {
        "product": product,
        "quantity": basket.exists(product)
    }
    return render(request, "store/detail.html", context=context)

def detail_window(request, slug):
    product = Product.objects.get(slug=slug)
    basket = Basket(request)
    print(product)
    context = {
        "product_name": product.name,
        "product_description": product.description,
        "product_price": product.price,
        "product_image": product.image.url,
        "product_url": product.get_absolute_url(),
        "product_add": product.get_absolute_url_for_add_to_basket(),
        "product_minus": product.get_absolute_url_for_remove_from_basket(),
        "quantity": basket.exists(product)
    }
    return HttpResponse(json.dumps(context), content_type="application/json")


def checkout_page(request):
    return render(request, "store/checkout.html")
