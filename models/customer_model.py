from pydantic import BaseModel, Field

class StripeCustomerResponse(BaseModel):
    """
    Pydantic schema to validate the HTTP response from Stripe's Customer endpoint.
    It strictly enforces data types and ensures the API contract is respected.
    """
    id: str
    object: str = Field(default="customer")
    email: str | None = None
    name: str | None = None
    balance: int = 0