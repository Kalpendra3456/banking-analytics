"""
==========================================================
Project     : Banking Analytics
File Name   : 12_transactions.py
Description : Generate realistic banking transactions
Author      : Kalpendra Yadav
==========================================================
"""

import random
import string
from datetime import datetime, timedelta

import pandas as pd
from faker import Faker

# ---------------------------------------------------------
# Configuration
# ---------------------------------------------------------

fake = Faker("en_IN")

random.seed(42)
Faker.seed(42)

NUM_ACCOUNTS = 20000
NUM_BENEFICIARIES = 40000
TOTAL_TRANSACTIONS = 500000

BANK_CODE = "BKAI"

# ---------------------------------------------------------
# Master Data
# ---------------------------------------------------------

TRANSACTION_TYPES = {

    1: "Cash Deposit",
    2: "Cash Withdrawal",
    3: "Online Transfer",
    4: "NEFT",
    5: "RTGS",
    6: "IMPS",
    7: "UPI",
    8: "Cheque Deposit",
    9: "Cheque Withdrawal",
    10: "Interest Credit",
    11: "Service Charge",
    12: "Loan EMI",
    13: "ATM Withdrawal",
    14: "Salary Credit",
    15: "Refund"

}

CHANNELS = [

    "ATM",
    "Branch",
    "Mobile Banking",
    "Internet Banking",
    "UPI",
    "POS",
    "System"

]

TRANSACTION_STATUS = [

    "Success",
    "Failed",
    "Pending",
    "Reversed"

]

CITIES = [

    "Mumbai",
    "Delhi",
    "Bengaluru",
    "Hyderabad",
    "Chennai",
    "Pune",
    "Ahmedabad",
    "Lucknow",
    "Jaipur",
    "Kolkata",
    "Noida",
    "Ghaziabad"

]

CITY_STATE = {

    "Mumbai": "Maharashtra",
    "Pune": "Maharashtra",
    "Delhi": "Delhi",
    "Bengaluru": "Karnataka",
    "Hyderabad": "Telangana",
    "Chennai": "Tamil Nadu",
    "Ahmedabad": "Gujarat",
    "Lucknow": "Uttar Pradesh",
    "Jaipur": "Rajasthan",
    "Kolkata": "West Bengal",
    "Noida": "Uttar Pradesh",
    "Ghaziabad": "Uttar Pradesh"

}

# ---------------------------------------------------------
# Helper Functions
# ---------------------------------------------------------

used_reference_numbers = set()

def generate_reference_number():

    while True:

        reference = (

            BANK_CODE +

            "".join(
                random.choices(
                    string.digits,
                    k=12
                )
            )

        )

        if reference not in used_reference_numbers:

            used_reference_numbers.add(reference)

            return reference


def generate_transaction_datetime():

    days = random.randint(0,730)

    seconds = random.randint(0,86399)

    transaction_date = (

        datetime.now()

        - timedelta(
            days=days,
            seconds=seconds
        )

    )

    return transaction_date.strftime("%Y-%m-%d %H:%M:%S")


def generate_amount():

    return round(

        random.choices(

            [

                random.uniform(100,1000),

                random.uniform(1000,10000),

                random.uniform(10000,50000),

                random.uniform(50000,500000)

            ],

            weights=[40,35,20,5]

        )[0],

        2

    )


def generate_balance(amount):

    balance = random.uniform(

        amount,

        1000000

    )

    return round(balance,2)

# ---------------------------------------------------------
# Transaction List
# ---------------------------------------------------------

transactions = []

transaction_id = 1 

# ---------------------------------------------------------
# Generate Transactions
# ---------------------------------------------------------

for _ in range(TOTAL_TRANSACTIONS):

    transaction_type_id = random.choices(

        [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],

        weights=[
            10,   # Cash Deposit
            8,    # Cash Withdrawal
            8,    # Online Transfer
            6,    # NEFT
            3,    # RTGS
            7,    # IMPS
            28,   # UPI
            2,    # Cheque Deposit
            1,    # Cheque Withdrawal
            5,    # Interest Credit
            4,    # Service Charge
            3,    # Loan EMI
            8,    # ATM Withdrawal
            5,    # Salary Credit
            2     # Refund
        ]

    )[0]

    amount = generate_amount()

    city = random.choice(CITIES)

    transaction = {

        "transaction_id": transaction_id,

        "transaction_reference":
            generate_reference_number(),

        "account_id":
            random.randint(1, NUM_ACCOUNTS),

        "beneficiary_id":
            random.randint(1, NUM_BENEFICIARIES),

        "transaction_type_id":
            transaction_type_id,

        "transaction_datetime":
            generate_transaction_datetime(),

        "transaction_amount":
            amount,

        "balance_after_transaction":
            generate_balance(amount),

        "channel":

            random.choices(

                CHANNELS,

                weights=[
                    8,   # ATM
                    10,  # Branch
                    28,  # Mobile Banking
                    18,  # Internet Banking
                    22,  # UPI
                    8,   # POS
                    6    # System
                ]

            )[0],

        "transaction_status":

            random.choices(

                TRANSACTION_STATUS,

                weights=[
                    96,
                    2,
                    1,
                    1
                ]

            )[0],

        "city": city,

        "state": CITY_STATE[city],

        "currency": "INR",

        "fraud_flag":

            random.choices(

                ["Yes","No"],

                weights=[
                    1,
                    999
                ]

            )[0],

        "remarks":

            TRANSACTION_TYPES[
                transaction_type_id
            ]

    }

    transactions.append(transaction)

    transaction_id += 1

# ---------------------------------------------------------
# Create DataFrame
# ---------------------------------------------------------

df = pd.DataFrame(transactions) 

# ---------------------------------------------------------
# Save CSV
# ---------------------------------------------------------

OUTPUT_PATH = "transactions.csv"

df.to_csv(
    OUTPUT_PATH,
    index=False,
    encoding="utf-8-sig"
)

# ---------------------------------------------------------
# Data Validation
# ---------------------------------------------------------

print("\nChecking Data Quality...\n")

print(f"Duplicate Transaction IDs      : {df['transaction_id'].duplicated().sum()}")
print(f"Duplicate Reference Numbers    : {df['transaction_reference'].duplicated().sum()}")

print("\nMissing Values")

print(df.isnull().sum())

# ---------------------------------------------------------
# Dataset Summary
# ---------------------------------------------------------

print("\nTransaction Type Distribution")

print(df["transaction_type_id"].value_counts().sort_index())

print("\nTransaction Status")

print(df["transaction_status"].value_counts())

print("\nChannel Distribution")

print(df["channel"].value_counts())

print("\nFraud Transactions")

print(df["fraud_flag"].value_counts())

print("\nTop 10 Cities")

print(df["city"].value_counts().head(10))

print("\nAverage Transaction Amount")

print(round(df["transaction_amount"].mean(), 2))

print("\nMaximum Transaction Amount")

print(round(df["transaction_amount"].max(), 2))

print("\nMinimum Transaction Amount")

print(round(df["transaction_amount"].min(), 2))

print("\nAverage Account Balance")

print(round(df["balance_after_transaction"].mean(), 2))

print("\nTotal Transaction Value")

print(round(df["transaction_amount"].sum(), 2))

# ---------------------------------------------------------
# Output
# ---------------------------------------------------------

print("=" * 60)
print("Transactions Generated Successfully")
print("=" * 60)

print(df.head())

print(f"\nTotal Transactions : {len(df):,}")
print(f"Total Columns      : {len(df.columns)}")
print(f"Saved To           : {OUTPUT_PATH}")

print("=" * 60)