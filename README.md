# 🚀 Stripe API Test Automation Framework

An enterprise-level, highly scalable API automation framework built to test Stripe's Customer and Payment Intent flows. Designed with FAANG-standard architecture, this project demonstrates advanced QA engineering practices.

## 🏗️ Architecture & Tech Stack

This framework is built using the **API Object Model** (similar to Page Object Model but for APIs) and strictly separates test logic from data layers.

* **Language:** Python 3
* **Test Runner:** Pytest
* **HTTP Client:** Requests
* **Data Validation:** Pydantic (Contract Testing)
* **Data Generation:** Faker (Dynamic payloads)
* **Reporting:** Allure Reports

## 🧠 Key Design Principles Applied

1. **Dependency Injection:** Utilizing Pytest `conftest.py` for seamless session management.
2. **State Management:** Strict Teardown processes (Every created data is deleted post-test).
3. **Data Contracts:** Using Pydantic models to catch silent schema changes and float/integer bugs.
4. **Boundary & Edge Testing:** Nested dictionary validation and max-limit validations.
5. **Dynamic Run Execution:** Custom `run_tests.py` to auto-generate timestamped Allure reports.

## 📂 Project Structure

```text
Stripe-API-Test-Automation/
├── api/                  # API Object Layer (Stripe endpoints)
├── core/                 # Core HTTP Client (Session & Auth management)
├── models/               # Pydantic Schemas (Data validation)
├── tests/                # Test Suites
│   ├── smoke/            # Health checks
│   ├── regression/       # End-to-end business flows
│   └── negative/         # Security & Boundary testing
├── utils/                # Helper tools (Faker data generation)
├── run_tests.py          # Custom execution engine
├── pytest.ini            # Framework configurations
└── requirements.txt      # Project dependencies
```

## ⚙️ How to Run Locally

**1. Clone the repository and install dependencies:**
```bash
pip install -r requirements.txt
```

**2. Setup your Environment Variables:**
Create a `.env` file in the root directory and add your Stripe Test Key:
```env
STRIPE_SECRET_KEY=sk_test_your_key_here
BASE_URL=https://api.stripe.com/v1
```

**3. Run the Automation Suite:**
```bash
python run_tests.py
```

**4. View the Allure Report:**
```bash
allure serve reports/allure-results/YYYY-MM-DD/HH-MM-SS
```

---
*Created as a demonstration of Quality Assurance Automation Engineering.*
