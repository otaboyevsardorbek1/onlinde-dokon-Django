from shop.settings import BASKET_SESSION
from store.models import Product

from django.db.models.query import QuerySet


class Basket:
    def __init__(self, request) -> None:
        self.session = request.session
        basket = self.session.get(BASKET_SESSION)

        if not basket:
            self.session[basket] = {}
            basket = self.session[basket]
        self.basket = basket

    def add(
        self,
        product: QuerySet,
        quantity: int = 1
    ) -> None:
        product_id = str(product.id)

        if product_id not in self.basket:
            self.basket[product_id] = {"quantity": quantity, "price": str(product.price)}
        else:
            self.basket[product_id]["quantity"] += quantity

        self.save()

    def remove(self, product):
        product_id = str(product.id)

        if product_id in self.basket:
            del self.basket[product_id]

            self.save()

    def clear(self):
        del self.session[BASKET_SESSION]

        self.save()

    def save(self):
        self.session[BASKET_SESSION] = self.basket
        self.session.modified = True

    def __iter__(self):
        product_ids = self.basket.keys()

        products = Product.objects.filter(id__in=product_ids)

        for product in products:
            self.basket[str(product.id)]["product"] = product

        for item in self.basket.values():
            item["total_price"] = item["price"] * item["quantity"]
             
            yield item

    def __len__(self) -> int:
        return sum(item["quantity"] for item in self.basket.values())

    def get_total_price(self) -> int:
        return sum(item["price"] for item in self.basket.values())
