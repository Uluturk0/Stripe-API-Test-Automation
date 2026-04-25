import os
import pytest
from datetime import datetime

# 1. Get the current date and time
current_time = datetime.now()

# Format: YYYY-MM-DD (e.g., 2026-04-25)
date_folder = current_time.strftime("%Y-%m-%d") 

# Format: HH-MM-SS (e.g., 14-30-05)
time_folder = current_time.strftime("%H-%M-%S") 

# 2. Define the dynamic path for Allure results
# This creates a nested structure: reports/allure-results/YYYY-MM-DD/HH-MM-SS
dynamic_allure_dir = os.path.join("reports", "allure-results", date_folder, time_folder)

print(f"\n=======================================================")
print(f"🚀 STARTING AUTOMATION SUITE")
print(f"📁 Reports will be saved to: {dynamic_allure_dir}")
print(f"=======================================================\n")

# 3. Execute Pytest programmatically with our dynamic arguments
exit_code = pytest.main([
    "-v", 
    "-s", 
    f"--alluredir={dynamic_allure_dir}"
])

print(f"\n[INFO] Test execution finished with exit code: {exit_code}")