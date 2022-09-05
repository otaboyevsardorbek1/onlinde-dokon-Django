from django.urls import path, include

from .views import home_page_view, basket_add, basket_detail


urlpatterns = [
    path("", home_page_view, name="home"),
    path("shop/", home_page_view, name="shop"),
    path("basket/add/<slug:slug>", basket_add, name='basket_add' ),
    path("basket-detail/", basket_detail, name='basket_detail' )
]
