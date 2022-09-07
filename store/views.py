from django.http import HttpResponseRedirect
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

def basket_remove_count(request, slug):
    
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
    return render(request, "store/detail.html")


def checkout_page(request):
    return render(request, "store/checkout.html")
