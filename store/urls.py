from django.urls import path, include

from .views import home_page_view, shop_page, detail_page, cart_page, checkout_page
 

urlpatterns = [
     path("", home_page_view, name="home"),
    path("shop/", shop_page, name="shop"),
    path("detail/", detail_page, name="detail"),
    path("cart/", cart_page, name="cart"),
    path("checkout/", checkout_page, name="checkout"),
]
