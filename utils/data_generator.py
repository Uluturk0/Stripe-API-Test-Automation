from faker import Faker

fake = Faker()

def generate_customer_payload() -> dict:
    """
    Generates random and unique customer data for Stripe API testing.
    This prevents data duplication errors during test execution.
    """
    return {
        "email": fake.email(),
        "name": fake.name(),
        "description": "Created by automated QA testing framework"
    }