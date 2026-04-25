from core.base_client import BaseClient

class StripeCustomersAPI:
    """
    API Object class for Stripe Customers endpoint.
    Abstracts the raw HTTP requests into meaningful business actions.
    """

    def __init__(self, client: BaseClient):
        self.client = client
        self.endpoint = "/customers"

    def create_customer(self, payload: dict | None = None):
        """Creates a new customer in Stripe."""
        return self.client.post(self.endpoint, payload=payload)

    def get_customer(self, customer_id: str):
        """Retrieves a specific customer by their ID."""
        return self.client.get(f"{self.endpoint}/{customer_id}")

    def update_customer(self, customer_id: str, payload: dict):
        """Updates an existing customer."""
        # Stripe uses POST to the specific ID for updates, not PUT
        return self.client.post(f"{self.endpoint}/{customer_id}", payload=payload)

    def delete_customer(self, customer_id: str):
        """Deletes a specific customer."""
        return self.client.delete(f"{self.endpoint}/{customer_id}")