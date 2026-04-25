import pytest
from core.base_client import BaseClient
from api.stripe_api import StripeCustomersAPI
from api.payment_api import StripePaymentsAPI

@pytest.fixture(scope="session")
def stripe_client():
    """
    Provides a reusable, authenticated Stripe client for the entire test session.
    """
    return BaseClient()

@pytest.fixture(scope="function")
def customer_setup(stripe_client):
    """
    A fixture that creates a temporary customer and deletes it after the test.
    This ensures our Stripe dashboard stays clean!
    """
    # 1. Setup: Create a customer
    payload = {"email": "test_fixture@example.com", "name": "Test Fixture User"}
    response = stripe_client.post("/customers", payload=payload)
    customer_id = response.json().get("id")
    
    yield customer_id
    
    # 2. Teardown: Delete the customer after the test ends
    stripe_client.delete(f"/customers/{customer_id}")

@pytest.fixture(scope="session")
def customers_api(stripe_client):
    """
    Injects the StripeCustomersAPI layer into our tests.
    It takes the base engine (stripe_client) and hands it to the API class.
    """
    return StripeCustomersAPI(stripe_client)

@pytest.fixture(scope="session")
def payments_api(stripe_client):
    """Injects the StripePaymentsAPI layer into our tests."""
    return StripePaymentsAPI(stripe_client)