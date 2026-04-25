import pytest
from models.payment_model import StripePaymentIntentResponse

class TestStripePayments:
    """
    Regression tests for the Checkout and Payment flows.
    """

    def test_create_valid_payment_intent(self, payments_api):
        """
        Simulates a user attempting to pay $50.00 for their shopping cart.
        """
        # 1. SETUP DATA ($50.00 is represented as 5000 cents)
        amount_in_cents = 5000
        currency = "usd"

        # 2. SEND REQUEST (Using our clean API layer)
        response = payments_api.create_payment_intent(amount=amount_in_cents, currency=currency)

        # 3. HTTP VALIDATION
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"

        # 4. PYDANTIC CONTRACT VALIDATION
        payment_data = response.json()
        payment = StripePaymentIntentResponse(**payment_data)

        # 5. BUSINESS LOGIC ASSERTIONS
        assert payment.amount == amount_in_cents
        assert payment.currency == currency
        
        # When a payment intent is just created, its status should be waiting for a card
        assert payment.status == "requires_payment_method"

        print(f"\n[SUCCESS] Payment Intent created! ID: {payment.id}, Amount: ${payment.amount/100} {payment.currency.upper()}")