"""
==========================================================
Project     : Banking Analytics
File Name   : 10_loan_payments.py
Description : Generate realistic loan payment data
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

TOTAL_LOANS = 5000

BANK_CODE = "BKAI"

# ---------------------------------------------------------
# Master Data
# ---------------------------------------------------------

PAYMENT_METHODS = [

    "Auto Debit",
    "UPI",
    "NEFT",
    "IMPS",
    "Cash",
    "Cheque"

]

PAYMENT_STATUS = [

    "Paid",
    "Late",
    "Missed"

]

# ---------------------------------------------------------
# Helper Functions
# ---------------------------------------------------------

used_payment_ids = set()

def generate_payment_reference():

    while True:

        ref = (

            BANK_CODE +
            "PAY" +
            str(random.randint(10000000,99999999))

        )

        if ref not in used_payment_ids:

            used_payment_ids.add(ref)

            return ref


def generate_payment_date():

    days = random.randint(0,730)

    payment_date = (

        datetime.today() -
        timedelta(days=days)

    )

    return payment_date


# ---------------------------------------------------------
# Loan Payment List
# ---------------------------------------------------------

loan_payments = []

payment_id = 1 

# ---------------------------------------------------------
# Generate Loan Payments
# ---------------------------------------------------------

for loan_id in range(1, TOTAL_LOANS + 1):

    # Number of EMIs paid for this loan
    total_payments = random.randint(12, 48)

    # Base EMI for this loan
    emi_amount = round(
        random.uniform(5000, 80000),
        2
    )

    # Initial Outstanding Balance
    remaining_balance = round(
        emi_amount * total_payments,
        2
    )

    payment_date = generate_payment_date()

    for emi_number in range(1, total_payments + 1):

        interest_paid = round(
            emi_amount * random.uniform(0.20, 0.45),
            2
        )

        principal_paid = round(
            emi_amount - interest_paid,
            2
        )

        late_fee = 0

        payment_status = random.choices(

            PAYMENT_STATUS,

            weights=[92,5,3]

        )[0]

        if payment_status == "Late":

            late_fee = random.randint(
                200,
                1500
            )

        elif payment_status == "Missed":

            late_fee = random.randint(
                500,
                3000
            )

        remaining_balance = max(

            0,

            round(
                remaining_balance -
                principal_paid,
                2
            )

        )

        payment = {

            "payment_id": payment_id,

            "payment_reference":
                generate_payment_reference(),

            "loan_id": loan_id,

            "emi_number": emi_number,

            "payment_date":
                payment_date.strftime("%Y-%m-%d"),

            "emi_amount": emi_amount,

            "principal_paid":
                principal_paid,

            "interest_paid":
                interest_paid,

            "late_fee":
                late_fee,

            "payment_method":

                random.choices(

                    PAYMENT_METHODS,

                    weights=[
                        40,  # Auto Debit
                        20,  # UPI
                        15,  # NEFT
                        10,  # IMPS
                        10,  # Cash
                        5    # Cheque
                    ]

                )[0],

            "payment_status":
                payment_status,

            "remaining_balance":
                remaining_balance

        }

        loan_payments.append(payment)

        payment_id += 1

        # Next month's EMI
        payment_date += timedelta(days=30)

# ---------------------------------------------------------
# Create DataFrame
# ---------------------------------------------------------

df = pd.DataFrame(loan_payments) 

# ---------------------------------------------------------
# Save CSV
# ---------------------------------------------------------

OUTPUT_PATH = "loan_payments.csv"

df.to_csv(
    OUTPUT_PATH,
    index=False,
    encoding="utf-8-sig"
)

# ---------------------------------------------------------
# Data Validation
# ---------------------------------------------------------

print("\nChecking Data Quality...\n")

print(f"Duplicate Payment IDs         : {df['payment_id'].duplicated().sum()}")
print(f"Duplicate Payment References  : {df['payment_reference'].duplicated().sum()}")

print("\nMissing Values")

print(df.isnull().sum())

# ---------------------------------------------------------
# Dataset Summary
# ---------------------------------------------------------

print("\nPayment Status")

print(df["payment_status"].value_counts())

print("\nPayment Methods")

print(df["payment_method"].value_counts())

print("\nAverage EMI Amount")

print(round(df["emi_amount"].mean(), 2))

print("\nAverage Principal Paid")

print(round(df["principal_paid"].mean(), 2))

print("\nAverage Interest Paid")

print(round(df["interest_paid"].mean(), 2))

print("\nAverage Late Fee")

print(round(df["late_fee"].mean(), 2))

print("\nMaximum EMI")

print(round(df["emi_amount"].max(), 2))

print("\nMinimum EMI")

print(round(df["emi_amount"].min(), 2))

print("\nTotal Principal Recovered")

print(round(df["principal_paid"].sum(), 2))

print("\nTotal Interest Collected")

print(round(df["interest_paid"].sum(), 2))

print("\nTotal Late Fees")

print(round(df["late_fee"].sum(), 2))

# ---------------------------------------------------------
# Output
# ---------------------------------------------------------

print("=" * 60)
print("Loan Payments Generated Successfully")
print("=" * 60)

print(df.head())

print(f"\nTotal Loan Payments : {len(df):,}")
print(f"Total Columns       : {len(df.columns)}")
print(f"Saved To            : {OUTPUT_PATH}")

print("=" * 60)