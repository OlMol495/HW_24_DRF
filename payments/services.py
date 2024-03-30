import stripe
from django.conf import settings


stripe.api_key = settings.STRIPE_SECRET_KEY


class StripeService:

    def __init__(self):
        self.stripe = stripe
        self.stripe.api_key = settings.STRIPE_SECRET_KEY

    def get_products(self):
        return self.stripe.Product.list()

    def create_product(self, name, price):
        product = self.stripe.Product.create(name=name)
        return self.stripe.Price.create(product=product.id, unit_amount=price * 100, currency='RUB')

    def create_session(self, price_id, base_url, course_id):

        return self.stripe.checkout.Session.create(payment_method_types=['card'],
            line_items=[{
                'price': price_id,
                'quantity': 1,
            }],
            mode='payment',
            success_url=base_url
                                                   )

