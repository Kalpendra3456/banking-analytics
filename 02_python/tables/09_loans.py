"""
==========================================================
Project     : Banking Analytics
File Name   : 09_loans.py
Description : Generate realistic loan data
Author      : Kalpendra Yadav
==========================================================
"""

import random
from datetime import datetime, timedelta

import pandas as pd

# ---------------------------------------------------------
# Configuration
# ---------------------------------------------------------

random.seed(42)

NUM_CUSTOMERS = 10000
NUM_ACCOUNTS = 20000
NUM_BRANCHES = 100
TOTAL_LOANS = 5000

BANK_CODE = "BKAI"

# ---------------------------------------------------------
# Loan Types
# ---------------------------------------------------------

LOAN_TYPES = {

    1: {
        "name": "Home Loan",
        "interest": (8.25, 10.50),
        "tenure": (120, 360)
    },

    2: {
        "name": "Personal Loan",
        "interest": (10.50, 18.00),
        "tenure": (12, 84)
    },

    3: {
        "name": "Car Loan",
        "interest": (8.75, 12.00),
        "tenure": (24, 84)
    },

    4: {
        "name": "Education Loan",
        "interest": (8.50, 12.50),
        "tenure": (24, 180)
    },

    5: {
        "name": "Gold Loan",
        "interest": (8.00, 11.00),
        "tenure": (6, 36)
    },

    6: {
        "name": "Business Loan",
        "interest": (11.00, 18.00),
        "tenure": (12, 120)
    },

    7: {
        "name": "MSME Loan",
        "interest": (9.50, 15.00),
        "tenure": (12, 180)
    },

    8: {
        "name": "Loan Against Property",
        "interest": (9.00, 12.50),
        "tenure": (60, 240)
    },

    9: {
        "name": "Two Wheeler Loan",
        "interest": (9.50, 14.00),
        "tenure": (12, 60)
    },

    10: {
        "name": "Agriculture Loan",
        "interest": (7.00, 10.00),
        "tenure": (12, 120)
    },

    11: {
        "name": "Commercial Vehicle Loan",
        "interest": (9.50, 13.50),
        "tenure": (24, 84)
    },

    12: {
        "name": "Working Capital Loan",
        "interest": (10.50, 16.50),
        "tenure": (6, 36)
    }

}

LOAN_STATUS = [
    "Active",
    "Closed",
    "Default"
]

PURPOSES = [
    "Home Purchase",
    "Business Expansion",
    "Education",
    "Medical",
    "Vehicle Purchase",
    "Working Capital",
    "Agriculture",
    "Personal Expenses"
]

# ---------------------------------------------------------
# Helper Functions
# ---------------------------------------------------------

used_loan_numbers = set()

def generate_loan_number():

    while True:

        loan_number = (
            BANK_CODE +
            "LN" +
            str(random.randint(10000000, 99999999))
        )

        if loan_number not in used_loan_numbers:

            used_loan_numbers.add(loan_number)

            return loan_number


def generate_disbursement_date():

    days = random.randint(365, 3650)

    return (
        datetime.today() -
        timedelta(days=days)
    )


def calculate_emi(principal, annual_rate, tenure):

    monthly_rate = annual_rate / 12 / 100

    emi = (
        principal
        * monthly_rate
        * (1 + monthly_rate) ** tenure
    ) / (
        (1 + monthly_rate) ** tenure - 1
    )

    return round(emi, 2)


# ---------------------------------------------------------
# Loan List
# ---------------------------------------------------------

loans = []

loan_id = 1 

# ---------------------------------------------------------
# Generate Loans
# ---------------------------------------------------------

for _ in range(TOTAL_LOANS):

    loan_type_id = random.randint(1, 12)

    loan_info = LOAN_TYPES[loan_type_id]

    interest_rate = round(
        random.uniform(
            loan_info["interest"][0],
            loan_info["interest"][1]
        ),
        2
    )

    tenure_months = random.randint(
        loan_info["tenure"][0],
        loan_info["tenure"][1]
    )

    # Loan Amount Distribution
    loan_amount = random.choices(

        [
            random.randint(50000, 500000),
            random.randint(500001, 2000000),
            random.randint(2000001, 5000000),
            random.randint(5000001, 10000000),
            random.randint(10000001, 50000000)
        ],

        weights=[25, 35, 25, 10, 5]

    )[0]

    emi_amount = calculate_emi(
        loan_amount,
        interest_rate,
        tenure_months
    )

    disbursement_date = generate_disbursement_date()

    maturity_date = (
        disbursement_date +
        timedelta(days=30 * tenure_months)
    )

    outstanding_balance = round(

        loan_amount *

        random.uniform(0.10, 1.00),

        2

    )

    collateral_value = (

        round(
            loan_amount *
            random.uniform(1.10, 1.80),
            2
        )

        if loan_type_id in [1,3,5,8,9,10,11]

        else 0

    )

    credit_score = random.randint(300, 900)

    if credit_score >= 750:
        risk = "Low"

    elif credit_score >= 650:
        risk = "Medium"

    else:
        risk = "High"

    loan = {

        "loan_id": loan_id,

        "loan_number": generate_loan_number(),

        "customer_id": random.randint(
            1,
            NUM_CUSTOMERS
        ),

        "account_id": random.randint(
            1,
            NUM_ACCOUNTS
        ),

        "loan_type_id": loan_type_id,

        "branch_id": random.randint(
            1,
            NUM_BRANCHES
        ),

        "loan_amount": loan_amount,

        "interest_rate": interest_rate,

        "tenure_months": tenure_months,

        "emi_amount": emi_amount,

        "outstanding_balance": outstanding_balance,

        "disbursement_date":
            disbursement_date.strftime("%Y-%m-%d"),

        "maturity_date":
            maturity_date.strftime("%Y-%m-%d"),

        "loan_status": random.choices(

            LOAN_STATUS,

            weights=[88,8,4]

        )[0],

        "collateral_value": collateral_value,

        "credit_score": credit_score,

        "purpose": random.choice(PURPOSES),

        "risk_category": risk

    }

    loans.append(loan)

    loan_id += 1

# ---------------------------------------------------------
# Create DataFrame
# ---------------------------------------------------------

df = pd.DataFrame(loans) 

# ---------------------------------------------------------
# Save CSV
# ---------------------------------------------------------

OUTPUT_PATH = "loans.csv"

df.to_csv(
    OUTPUT_PATH,
    index=False,
    encoding="utf-8-sig"
)

# ---------------------------------------------------------
# Data Validation
# ---------------------------------------------------------

print("\nChecking Data Quality...\n")

print(f"Duplicate Loan IDs          : {df['loan_id'].duplicated().sum()}")
print(f"Duplicate Loan Numbers      : {df['loan_number'].duplicated().sum()}")

print("\nMissing Values")

print(df.isnull().sum())

# ---------------------------------------------------------
# Dataset Summary
# ---------------------------------------------------------

print("\nLoan Status")

print(df["loan_status"].value_counts())

print("\nRisk Category")

print(df["risk_category"].value_counts())

print("\nLoan Type Distribution")

print(df["loan_type_id"].value_counts().sort_index())

print("\nAverage Loan Amount")

print(round(df["loan_amount"].mean(), 2))

print("\nAverage EMI")

print(round(df["emi_amount"].mean(), 2))

print("\nAverage Interest Rate")

print(round(df["interest_rate"].mean(), 2))

print("\nAverage Credit Score")

print(round(df["credit_score"].mean(), 2))

print("\nMaximum Loan Amount")

print(df["loan_amount"].max())

print("\nMinimum Loan Amount")

print(df["loan_amount"].min())

print("\nTotal Loan Portfolio")

print(round(df["loan_amount"].sum(), 2))

print("\nOutstanding Loan Balance")

print(round(df["outstanding_balance"].sum(), 2))

# ---------------------------------------------------------
# Output
# ---------------------------------------------------------

print("=" * 60)
print("Loans Generated Successfully")
print("=" * 60)

print(df.head())

print(f"\nTotal Loans   : {len(df):,}")
print(f"Total Columns : {len(df.columns)}")
print(f"Saved To      : {OUTPUT_PATH}")

print("=" * 60)