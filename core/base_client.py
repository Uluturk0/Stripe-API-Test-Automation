import os
import requests
from dotenv import load_dotenv
from tenacity import retry, stop_after_attempt, wait_fixed

# Load environment variables from the .env file secretly
load_dotenv()

class BaseClient:
    """
    The advanced core engine for interacting with the Stripe API.
    Combines central routing, retry mechanisms, and Stripe's specific data encoding.
    """

    def __init__(self):
        self.base_url = os.getenv("BASE_URL")
        self.api_key = os.getenv("STRIPE_SECRET_KEY")
        
        self.session = requests.Session()
        self.headers = self.session.headers
        # Stripe Authentication uses Bearer Token
        # Stripe requires 'application/x-www-form-urlencoded' for data mutations
        self.session.headers.update({
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/x-www-form-urlencoded"
        })

    @retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
    def _send_request(self, method: str, endpoint: str, payload: dict | None = None, **kwargs) -> requests.Response:
        """
        Centralized request router with built-in retry logic.
        Automatically handles Stripe's form-encoded data requirements.
        """
        url = f"{self.base_url}{endpoint}"
        
        # We use 'data=payload' here because Stripe strictly forbids 'json=payload'
        response = self.session.request(
            method=method,
            url=url,
            data=payload,
            **kwargs
        )
        
        return response

    def get(self, endpoint: str, params: dict | None = None, **kwargs) -> requests.Response:
        """Executes a GET request."""
        return self._send_request(method="GET", endpoint=endpoint, params=params, **kwargs)

    def post(self, endpoint: str, payload: dict | None = None, **kwargs) -> requests.Response:
        """Executes a POST request (Used for creation AND updating in Stripe)."""
        return self._send_request(method="POST", endpoint=endpoint, payload=payload, **kwargs)

    def delete(self, endpoint: str, **kwargs) -> requests.Response:
        """Executes a DELETE request (Used for cleaning up test data)."""
        return self._send_request(method="DELETE", endpoint=endpoint, **kwargs)