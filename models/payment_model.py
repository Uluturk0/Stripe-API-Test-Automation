from pydantic import BaseModel, Field

class StripePaymentIntentResponse(BaseModel):
    """
    Validates the PaymentIntent response from Stripe.
    Ensures money values (amount) are always integers (cents) to prevent decimal bugs!
    """
    id: str
    object: str = Field(default="payment_intent")
    amount: int
    currency: str
    status: str