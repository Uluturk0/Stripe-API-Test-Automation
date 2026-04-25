from core.base_client import BaseClient

class StripePaymentsAPI:
    """
    API Object class for Stripe PaymentIntents.
    """

    def __init__(self, client: BaseClient):
        self.client = client
        self.endpoint = "/payment_intents"

    def create_payment_intent(self, amount: int, currency: str = "usd", **kwargs):
        """
        Creates a request to charge a customer.
        We make 'currency' default to USD so we don't have to type it every time.
        """
        payload = {
            "amount": amount,
            "currency": currency,
            **kwargs
        }
        return self.client.post(self.endpoint, payload=payload)