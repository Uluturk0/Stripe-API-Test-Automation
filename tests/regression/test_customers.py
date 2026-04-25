import pytest
from utils.data_generator import generate_customer_payload
from models.customer_model import StripeCustomerResponse

class TestStripeCustomers:
    """
    Comprehensive regression tests for the Customer lifecycle in Stripe.
    """

    def test_create_and_validate_new_customer(self, customers_api):
        payload = generate_customer_payload()
        response = customers_api.create_customer(payload=payload)
        
        assert response.status_code == 200
        
        response_data = response.json()
        customer = StripeCustomerResponse(**response_data)
        
        assert customer.object == "customer"
        assert customer.email == payload["email"]
        assert customer.name == payload["name"]
        
        print(f"\n[SUCCESS] Customer '{customer.name}' created with ID: {customer.id}")
        
        delete_response = customers_api.delete_customer(customer.id)
        assert delete_response.status_code == 200

    def test_update_existing_customer(self, customers_api):
        # 1. SETUP
        initial_payload = generate_customer_payload()
        create_response = customers_api.create_customer(payload=initial_payload)
        customer_id = create_response.json()["id"]

        # 2. ACTION
        update_payload = {"name": "Updated Name By Automation"}
        update_response = customers_api.update_customer(customer_id=customer_id, payload=update_payload)
        
        # 3. VALIDATION
        assert update_response.status_code == 200
        
        updated_data = update_response.json()
        updated_customer = StripeCustomerResponse(**updated_data)
        
        assert updated_customer.name == "Updated Name By Automation"
        assert updated_customer.id == customer_id
        
        print(f"\n[SUCCESS] Customer {customer_id} name updated successfully.")

        # 4. TEARDOWN
        customers_api.delete_customer(customer_id)

    def test_create_customer_with_nested_metadata(self, customers_api):
        """
        Tests if the API correctly stores and returns nested dictionary objects.
        """
        payload = generate_customer_payload()
        
        # FIX: How x-www-form-urlencoded expects nested objects in Stripe
        payload["metadata[internal_erp_id]"] = "ERP-999888"
        payload["metadata[customer_tier]"] = "VIP_GOLD"
        payload["metadata[marketing_opt_in]"] = "true"

        response = customers_api.create_customer(payload=payload)
        
        # Now it will successfully return 200
        assert response.status_code == 200

        customer_data = response.json()
        
        assert "metadata" in customer_data
        assert customer_data["metadata"]["internal_erp_id"] == "ERP-999888"
        assert customer_data["metadata"]["customer_tier"] == "VIP_GOLD"
        
        print(f"\n[SUCCESS] Nested Metadata validated successfully for ID: {customer_data['id']}")

        customers_api.delete_customer(customer_data["id"])