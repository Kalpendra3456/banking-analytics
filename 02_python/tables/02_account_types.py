"""
==========================================================
Project     : Banking Analytics
File Name   : 02_account_types.py
Description : Generate account types master table
Author      : Kalpendra Yadav
==========================================================
"""

import pandas as pd

# ---------------------------------------------------------
# Account Types Data
# ---------------------------------------------------------

account_types = [
    {
        "account_type_id": 1,
        "account_type": "Savings Account",
        "category": "Deposit",
        "minimum_balance": 1000,
        "interest_rate": 3.50,
        "status": "Active"
    },
    {
        "account_type_id": 2,
        "account_type": "Current Account",
        "category": "Deposit",
        "minimum_balance": 10000,
        "interest_rate": 0.00,
        "status": "Active"
    },
    {
        "account_type_id": 3,
        "account_type": "Salary Account",
        "category": "Deposit",
        "minimum_balance": 0,
        "interest_rate": 3.00,
        "status": "Active"
    },
    {
        "account_type_id": 4,
        "account_type": "Fixed Deposit",
        "category": "Deposit",
        "minimum_balance": 5000,
        "interest_rate": 6.75,
        "status": "Active"
    },
    {
        "account_type_id": 5,
        "account_type": "Recurring Deposit",
        "category": "Deposit",
        "minimum_balance": 500,
        "interest_rate": 6.25,
        "status": "Active"
    },
    {
        "account_type_id": 6,
        "account_type": "NRE Account",
        "category": "NRI",
        "minimum_balance": 10000,
        "interest_rate": 3.50,
        "status": "Active"
    },
    {
        "account_type_id": 7,
        "account_type": "NRO Account",
        "category": "NRI",
        "minimum_balance": 10000,
        "interest_rate": 3.50,
        "status": "Active"
    },
    {
        "account_type_id": 8,
        "account_type": "Joint Account",
        "category": "Deposit",
        "minimum_balance": 2000,
        "interest_rate": 3.50,
        "status": "Active"
    },
    {
        "account_type_id": 9,
        "account_type": "Senior Citizen Savings",
        "category": "Deposit",
        "minimum_balance": 1000,
        "interest_rate": 4.00,
        "status": "Active"
    },
    {
        "account_type_id": 10,
        "account_type": "Student Account",
        "category": "Deposit",
        "minimum_balance": 0,
        "interest_rate": 3.50,
        "status": "Active"
    }
]

# ---------------------------------------------------------
# DataFrame
# ---------------------------------------------------------

df = pd.DataFrame(account_types)

# ---------------------------------------------------------
# Save CSV
# ---------------------------------------------------------

OUTPUT_PATH = "account_types.csv"

df.to_csv(
    OUTPUT_PATH,
    index=False,
    encoding="utf-8-sig"
)

print("=" * 60)
print("Account Types Generated Successfully")
print("=" * 60)
print(df)
print(f"\nTotal Account Types : {len(df)}")
print(f"Saved To            : {OUTPUT_PATH}")