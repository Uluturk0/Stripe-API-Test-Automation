import pytest
from core.base_client import BaseClient

class TestNegativeScenarios:
    """
    Negative testing: Ensuring the system fails gracefully under invalid conditions.
    """

    def test_unauthorized_access_with_invalid_token(self):
        hacker_client = BaseClient()
        hacker_client.session.headers["Authorization"] = "Bearer sk_test_fake_hacker_key_12345"

        response = hacker_client.get("/customers")

        assert response.status_code == 401
        
        error_data = response.json()
        assert "error" in error_data
        assert error_data["error"]["type"] == "invalid_request_error"
        
        print("\n[SUCCESS] Security block verified! Invalid token returned 401.")

    def test_payment_with_negative_amount(self, payments_api):
        negative_amount = -5000

        response = payments_api.create_payment_intent(amount=negative_amount, currency="usd")

        assert response.status_code == 400

        error_data = response.json()
        assert error_data["error"]["type"] == "invalid_request_error"
        assert error_data["error"]["param"] == "amount"
        
        print("\n[SUCCESS] Data validation verified! Negative amount returned 400.")

    def test_payment_with_invalid_currency(self, payments_api):
        response = payments_api.create_payment_intent(amount=2000, currency="xyz")

        assert response.status_code == 400

        error_data = response.json()
        assert error_data["error"]["type"] == "invalid_request_error"
        assert error_data["error"]["param"] == "currency"
        
        print("\n[SUCCESS] Invalid currency blocked successfully. Returned 400.")
   
    def test_payment_amount_exceeds_maximum_limit(self, payments_api):
        """
        Boundary Value Analysis Test: Attempting to process a transaction 
        larger than Stripe's allowed maximum limit.
        """
        massive_amount = 10000000000 # 10 Billion cents
        response = payments_api.create_payment_intent(amount=massive_amount, currency="usd")

        assert response.status_code == 400

        error_data = response.json()
        assert error_data["error"]["type"] == "invalid_request_error"
        # FIX: Stripe uses 'code' instead of 'param' for maximum limit errors
        assert error_data["error"]["code"] == "amount_too_large"
        
        print("\n[SUCCESS] Boundary limits verified! Absurdly large amount returned 400.")