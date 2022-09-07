from django.urls import path, include

from .views import (
    home_page_view,
    shop_page_view,
    detail_page,
    cart_page,
    checkout_page,
    basket_add,
    basket_remove,
    basket_remove_count,
)


urlpatterns = [
    path("", home_page_view, name="home"),
    path("shop/", shop_page_view, name="shop"),
    path("detail/<slug:slug>", detail_page, name="detail"),
    path("cart/", cart_page, name="cart"),
    path("checkout/", checkout_page, name="checkout"),
    path("basket/add/<slug:slug>", basket_add, name="basket_add"),
    path("basket/remove/<slug:slug>", basket_remove, name="basket_remove"),
    path("basket/remove/count/<slug:slug>", basket_remove_count, name="basket_remove_count"),
]
