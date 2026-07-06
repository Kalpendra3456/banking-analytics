"""
==========================================================
Project     : Banking Analytics
File Name   : 03_loan_types.py
Description : Generate loan types master data
Author      : Kalpendra Yadav
==========================================================
"""

import pandas as pd

# ---------------------------------------------------------
# Loan Types Master Data
# ---------------------------------------------------------

loan_types = [
    {
        "loan_type_id": 1,
        "loan_type": "Home Loan",
        "category": "Housing",
        "secured": "Yes",
        "max_tenure_months": 360,
        "interest_rate_min": 8.25,
        "interest_rate_max": 10.50,
        "processing_fee_percent": 0.50,
        "status": "Active"
    },
    {
        "loan_type_id": 2,
        "loan_type": "Personal Loan",
        "category": "Personal",
        "secured": "No",
        "max_tenure_months": 84,
        "interest_rate_min": 10.50,
        "interest_rate_max": 18.00,
        "processing_fee_percent": 2.00,
        "status": "Active"
    },
    {
        "loan_type_id": 3,
        "loan_type": "Car Loan",
        "category": "Vehicle",
        "secured": "Yes",
        "max_tenure_months": 84,
        "interest_rate_min": 8.75,
        "interest_rate_max": 12.00,
        "processing_fee_percent": 1.00,
        "status": "Active"
    },
    {
        "loan_type_id": 4,
        "loan_type": "Education Loan",
        "category": "Education",
        "secured": "No",
        "max_tenure_months": 180,
        "interest_rate_min": 8.50,
        "interest_rate_max": 12.50,
        "processing_fee_percent": 0.50,
        "status": "Active"
    },
    {
        "loan_type_id": 5,
        "loan_type": "Gold Loan",
        "category": "Gold",
        "secured": "Yes",
        "max_tenure_months": 36,
        "interest_rate_min": 8.00,
        "interest_rate_max": 11.00,
        "processing_fee_percent": 0.50,
        "status": "Active"
    },
    {
        "loan_type_id": 6,
        "loan_type": "Business Loan",
        "category": "Business",
        "secured": "No",
        "max_tenure_months": 120,
        "interest_rate_min": 11.00,
        "interest_rate_max": 18.00,
        "processing_fee_percent": 2.00,
        "status": "Active"
    },
    {
        "loan_type_id": 7,
        "loan_type": "MSME Loan",
        "category": "Business",
        "secured": "No",
        "max_tenure_months": 180,
        "interest_rate_min": 9.50,
        "interest_rate_max": 15.00,
        "processing_fee_percent": 1.50,
        "status": "Active"
    },
    {
        "loan_type_id": 8,
        "loan_type": "Loan Against Property",
        "category": "Mortgage",
        "secured": "Yes",
        "max_tenure_months": 240,
        "interest_rate_min": 9.00,
        "interest_rate_max": 12.50,
        "processing_fee_percent": 1.00,
        "status": "Active"
    },
    {
        "loan_type_id": 9,
        "loan_type": "Two Wheeler Loan",
        "category": "Vehicle",
        "secured": "Yes",
        "max_tenure_months": 60,
        "interest_rate_min": 9.50,
        "interest_rate_max": 14.00,
        "processing_fee_percent": 1.00,
        "status": "Active"
    },
    {
        "loan_type_id": 10,
        "loan_type": "Agriculture Loan",
        "category": "Agriculture",
        "secured": "Yes",
        "max_tenure_months": 120,
        "interest_rate_min": 7.00,
        "interest_rate_max": 10.00,
        "processing_fee_percent": 0.25,
        "status": "Active"
    },
    {
        "loan_type_id": 11,
        "loan_type": "Commercial Vehicle Loan",
        "category": "Vehicle",
        "secured": "Yes",
        "max_tenure_months": 84,
        "interest_rate_min": 9.50,
        "interest_rate_max": 13.50,
        "processing_fee_percent": 1.25,
        "status": "Active"
    },
    {
        "loan_type_id": 12,
        "loan_type": "Working Capital Loan",
        "category": "Business",
        "secured": "No",
        "max_tenure_months": 36,
        "interest_rate_min": 10.50,
        "interest_rate_max": 16.50,
        "processing_fee_percent": 1.50,
        "status": "Active"
    }
]

# ---------------------------------------------------------
# Create DataFrame
# ---------------------------------------------------------

df = pd.DataFrame(loan_types)

# ---------------------------------------------------------
# Save CSV
# ---------------------------------------------------------

OUTPUT_PATH = "loan_types.csv"

df.to_csv(
    OUTPUT_PATH,
    index=False,
    encoding="utf-8-sig"
)

# ---------------------------------------------------------
# Output
# ---------------------------------------------------------

print("=" * 60)
print("Loan Types Generated Successfully")
print("=" * 60)
print(df)

from pathlib import Path

print(f"Saved To                : {Path(OUTPUT_PATH).resolve()}")