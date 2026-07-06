"""
==========================================================
Project     : Banking Analytics
File Name   : 06_accounts.py
Description : Generate realistic bank accounts
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

ACCOUNT_TYPES = {
    1: ("Savings Account", 3.50),
    2: ("Current Account", 0.00),
    3: ("Salary Account", 3.00),
    4: ("Fixed Deposit", 6.75),
    5: ("Recurring Deposit", 6.25),
    6: ("NRE Account", 3.50),
    7: ("NRO Account", 3.50),
    8: ("Joint Account", 3.50),
    9: ("Senior Citizen Savings", 4.00),
    10: ("Student Account", 3.50)
}

ACCOUNT_STATUS = [
    "Active",
    "Dormant",
    "Frozen",
    "Closed"
]

used_account_numbers = set()

accounts = []

# ---------------------------------------------------------
# Helper Functions
# ---------------------------------------------------------

def generate_account_number():

    while True:

        number = str(random.randint(100000000000, 999999999999))

        if number not in used_account_numbers:
            used_account_numbers.add(number)
            return number


def generate_opening_date():

    years = random.randint(0, 15)

    return (
        datetime.today() -
        timedelta(days=years * 365)
    ).strftime("%Y-%m-%d")


def generate_last_transaction():

    days = random.randint(0, 180)

    return (
        datetime.today() -
        timedelta(days=days)
    ).strftime("%Y-%m-%d")


def generate_balance():

    return random.choices(

        [
            random.randint(0, 10000),
            random.randint(10001, 50000),
            random.randint(50001, 200000),
            random.randint(200001, 1000000),
            random.randint(1000001, 5000000)
        ],

        weights=[15, 35, 30, 15, 5]

    )[0]

# ---------------------------------------------------------
# Generate Accounts
# ---------------------------------------------------------

account_id = 1

for customer_id in range(1, NUM_CUSTOMERS + 1):

    # Number of accounts per customer
    number_of_accounts = random.choices(
        [1, 2, 3],
        weights=[70, 25, 5]
    )[0]

    for _ in range(number_of_accounts):

        account_type_id = random.choices(
            [1,2,3,4,5,6,7,8,9,10],
            weights=[60,15,15,3,2,1,1,1,1,1]
        )[0]

        interest_rate = ACCOUNT_TYPES[account_type_id][1]

        balance = generate_balance()

        account = {

            "account_id": account_id,

            "account_number": generate_account_number(),

            "customer_id": customer_id,

            "account_type_id": account_type_id,

            "branch_id": random.randint(1,100),

            "opening_date": generate_opening_date(),

            "current_balance": balance,

            "available_balance": round(
                balance - random.randint(0,5000),
                2
            ),

            "account_status": random.choices(
                ACCOUNT_STATUS,
                weights=[92,5,2,1]
            )[0],

            "currency": "INR",

            "nominee_registered": random.choices(
                ["Yes","No"],
                weights=[90,10]
            )[0],

            "internet_banking": random.choices(
                ["Yes","No"],
                weights=[75,25]
            )[0],

            "mobile_banking": random.choices(
                ["Yes","No"],
                weights=[82,18]
            )[0],

            "debit_card": random.choices(
                ["Yes","No"],
                weights=[96,4]
            )[0],

            "cheque_book": random.choices(
                ["Yes","No"],
                weights=[65,35]
            )[0],

            "last_transaction_date": generate_last_transaction(),

            "average_monthly_balance": round(
                balance * random.uniform(0.70,1.10),
                2
            ),

            "interest_rate": interest_rate,

            "account_rating": random.choices(
                ["Excellent","Good","Average","Poor"],
                weights=[15,50,25,10]
            )[0]

        }

        accounts.append(account)

        account_id += 1

# ---------------------------------------------------------
# Create DataFrame
# ---------------------------------------------------------

df = pd.DataFrame(accounts)

# ---------------------------------------------------------
# Save CSV
# ---------------------------------------------------------

OUTPUT_PATH = "accounts.csv"

df.to_csv(
    OUTPUT_PATH,
    index=False,
    encoding="utf-8-sig"
)

# ---------------------------------------------------------
# Data Validation
# ---------------------------------------------------------

print("\nChecking Data Quality...\n")

print(f"Duplicate Account IDs       : {df['account_id'].duplicated().sum()}")
print(f"Duplicate Account Numbers   : {df['account_number'].duplicated().sum()}")

print("\nMissing Values")

print(df.isnull().sum())

# ---------------------------------------------------------
# Dataset Summary
# ---------------------------------------------------------

print("\nAccount Types")

print(df["account_type_id"].value_counts().sort_index())

print("\nAccount Status")

print(df["account_status"].value_counts())

print("\nCurrency")

print(df["currency"].value_counts())

print("\nInternet Banking")

print(df["internet_banking"].value_counts())

print("\nMobile Banking")

print(df["mobile_banking"].value_counts())

print("\nDebit Card")

print(df["debit_card"].value_counts())

print("\nCheque Book")

print(df["cheque_book"].value_counts())

print("\nNominee Registered")

print(df["nominee_registered"].value_counts())

print("\nAverage Balance")

print(round(df["current_balance"].mean(), 2))

print("\nMaximum Balance")

print(df["current_balance"].max())

print("\nMinimum Balance")

print(df["current_balance"].min())

# ---------------------------------------------------------
# Output
# ---------------------------------------------------------

print("=" * 60)
print("Accounts Generated Successfully")
print("=" * 60)

print(df.head())

print(f"\nTotal Accounts : {len(df):,}")
print(f"Total Columns  : {len(df.columns)}")
print(f"Saved To       : {OUTPUT_PATH}")

print("=" * 60)