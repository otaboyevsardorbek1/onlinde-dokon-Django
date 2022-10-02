from shop.settings import BASKET_SESSION, STRIPE_SECRET_KEY
from store.models import Product

import stripe

from django.db.models.query import QuerySet
from django.urls import reverse

class Basket:
    def __init__(self, request) -> None:
        self.session = request.session
        basket = self.session.get(BASKET_SESSION)

        if not basket and not basket == {}:
            self.session[basket] = {}
            basket = self.session[basket]
        self.basket = basket

    def add(self, product: QuerySet, quantity: int = 1) -> None:
        product_id = str(product.id)
        print(product)
        print(self.basket)

        if product_id not in self.basket:
            self.basket[product_id] = {
                "quantity": quantity,
                "price": str(product.price),
            }
        else:
            self.basket[product_id]["quantity"] += quantity

        self.save()

    def remove_count(self, product: QuerySet, quantity: int = 1) -> None:
        product_id = str(product.id)

        if product_id in self.basket:

            if self.basket[product_id]["quantity"] > 1:

                self.basket[product_id]["quantity"] -= quantity
                self.save()
            else:
                self.remove(product)

    def remove(self, product):
        product_id = str(product.id)

        if product_id in self.basket:
            del self.basket[product_id]

            self.save()

    def clear(self):
        self.basket = {}

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
            item["total_price"] = int(item["price"]) * item["quantity"]

            yield item

    def __len__(self) -> int:
        if self.basket:
            return sum(item["quantity"] for item in self.basket.values())
        else:
            return 0

    def exists(self, product) -> int:
        product_id = product.id
        for product in self.basket:
            if int(product) == product_id:
                return self.basket[product]["quantity"]
        return 0

    def get_total_price(self) -> int:
        return sum(
            [int(item["price"]) * item["quantity"] for item in self.basket.values()]
        )


class StripeService:
    def __init__(self) -> None:
        self.stripe = stripe
        self.stripe.api_key = STRIPE_SECRET_KEY

    def generate_product_card(self, products):
        product_items = []
        for product in products:
            product_items.append(
                {
                    "price_data": {
                        "currency": "usd",
                        "product_data": {
                            "name": product["product"].name,
                            "description": product["product"].description,
                        },
                        "unit_amount": product["product"].price * 100,
                    },
                    "quantity": product["quantity"],
                },
            )
        return product_items

    def checkout(self, request, products):

        session = self.stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=self.generate_product_card(products=products),
            mode="payment",
            success_url=request.build_absolute_uri(reverse('home')+"?session_id={CHECKOUT_SESSION_ID}"),
            cancel_url=request.build_absolute_uri(reverse("cart"))
        )

        return session.id
    
    def get_detail_by_session_id(self, session_id):
        data =  self.stripe.checkout.Session.retrieve(session_id)
        name = data["customer_details"]["name"]
        email = data["customer_deatils"]["email"]

        return name, email

