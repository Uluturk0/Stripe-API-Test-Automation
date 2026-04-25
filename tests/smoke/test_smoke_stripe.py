import pytest

class TestSmokeStripe:
    """
    Smoke tests to verify basic system health, connectivity, and authentication.
    """

    def test_stripe_api_is_alive(self, stripe_client):
        """
        Sends a basic GET request to the customers endpoint to verify 
        the API is reachable and our Secret Key is valid.
        """
        # We inject the 'stripe_client' from our conftest.py automatically
        response = stripe_client.get("/customers")
        
        # If this fails, the API is down or our credentials are wrong
        assert response.status_code == 200, f"Smoke test failed! Status Code: {response.status_code}"
        
        print("\n[SUCCESS] Stripe API is reachable and authentication is working perfectly!")