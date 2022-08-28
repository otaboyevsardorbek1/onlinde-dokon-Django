from django.http import HttpResponseRedirect
from django.shortcuts import render


from store.business_logic.selectors import get_all_category, get_all_products
from store.models import Basket, Product


def home_page_view(request):
    context = {
        "category": get_all_category(),
        "products": get_all_products(),
    }
    return render(request, "store/index.html", context=context)


def basket_add(request, product_slag):
    current_page = request.META.get("HTTP_REFERER")
    product = Product.objects.get(slug=product_slag)
    baskets, created = Basket.objects.get_or_create(user=request.user, product=product)

    if not created:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()
    return HttpResponseRedirect(current_page)

def shopping_page_view(request):
    return render(request, "store/shop.html")
