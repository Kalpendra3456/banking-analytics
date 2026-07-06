"""
==========================================================
Project     : Banking Analytics
File Name   : 11_credit_cards.py
Description : Generate realistic credit card data
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

# Number of customers
NUM_CUSTOMERS = 10000

# Number of accounts
NUM_ACCOUNTS = 20000

# Approximately 45% of customers have a credit card
CARD_HOLDERS = 4500

BANK_NAME = "BankAI"

# ---------------------------------------------------------
# Master Data
# ---------------------------------------------------------

CARD_TYPES = [
    "Classic",
    "Gold",
    "Platinum",
    "Signature"
]

CARD_NETWORKS = [
    "Visa",
    "Mastercard",
    "RuPay",
    "American Express"
]

CARD_STATUS = [
    "Active",
    "Blocked",
    "Expired",
    "Closed"
]

# ---------------------------------------------------------
# Helper Functions
# ---------------------------------------------------------

used_card_numbers = set()

def generate_card_number():

    while True:

        number = (
            "4" +
            "".join(
                random.choices(
                    "0123456789",
                    k=15
                )
            )
        )

        if number not in used_card_numbers:

            used_card_numbers.add(number)

            return number


def generate_expiry_date():

    years = random.randint(2, 5)

    expiry = datetime.today() + timedelta(days=365 * years)

    return expiry.strftime("%m/%y")


def generate_issue_date():

    years = random.randint(0, 5)

    issue = datetime.today() - timedelta(days=365 * years)

    return issue.strftime("%Y-%m-%d")


def generate_due_date():

    due = datetime.today() + timedelta(days=random.randint(5, 30))

    return due.strftime("%Y-%m-%d")


def generate_credit_limit():

    return random.choices(

        [
            50000,
            100000,
            200000,
            500000,
            1000000
        ],

        weights=[35, 30, 20, 10, 5]

    )[0]

# ---------------------------------------------------------
# Credit Card List
# ---------------------------------------------------------

credit_cards = []

card_id = 1

# ---------------------------------------------------------
# Generate Credit Cards
# ---------------------------------------------------------

for customer_id in random.sample(
    range(1, NUM_CUSTOMERS + 1),
    CARD_HOLDERS
):

    credit_limit = generate_credit_limit()

    outstanding_balance = round(
        credit_limit * random.uniform(0.00, 0.95),
        2
    )

    available_credit = round(
        credit_limit - outstanding_balance,
        2
    )

    card_type = random.choices(
        CARD_TYPES,
        weights=[45, 30, 20, 5]
    )[0]

    card = {

        "card_id": card_id,

        "card_number": generate_card_number(),

        "customer_id": customer_id,

        # Customer may have multiple accounts
        "account_id": random.randint(1, NUM_ACCOUNTS),

        "card_type": card_type,

        "card_network": random.choices(
            CARD_NETWORKS,
            weights=[45, 35, 15, 5]
        )[0],

        "credit_limit": credit_limit,

        "available_credit": available_credit,

        "outstanding_balance": outstanding_balance,

        "billing_day": random.randint(1, 28),

        "payment_due_date": generate_due_date(),

        "minimum_due": round(
            outstanding_balance * 0.05,
            2
        ),

        "interest_rate": round(
            random.uniform(30.0, 48.0),
            2
        ),

        "cash_limit": round(
            credit_limit * 0.30,
            2
        ),

        "reward_points": random.randint(0, 25000),

        "cvv": random.randint(100, 999),

        "issue_date": generate_issue_date(),

        "expiry_date": generate_expiry_date(),

        "contactless_enabled": random.choices(
            ["Yes", "No"],
            weights=[90, 10]
        )[0],

        "international_usage": random.choices(
            ["Enabled", "Disabled"],
            weights=[30, 70]
        )[0],

        "card_status": random.choices(
            CARD_STATUS,
            weights=[94, 2, 2, 2]
        )[0]

    }

    credit_cards.append(card)

    card_id += 1

# ---------------------------------------------------------
# Create DataFrame
# ---------------------------------------------------------

df = pd.DataFrame(credit_cards) 

# ---------------------------------------------------------
# Save CSV
# ---------------------------------------------------------

OUTPUT_PATH = "credit_cards.csv"

df.to_csv(
    OUTPUT_PATH,
    index=False,
    encoding="utf-8-sig"
)

# ---------------------------------------------------------
# Data Validation
# ---------------------------------------------------------

print("\nChecking Data Quality...\n")

print(f"Duplicate Card IDs        : {df['card_id'].duplicated().sum()}")
print(f"Duplicate Card Numbers    : {df['card_number'].duplicated().sum()}")

print("\nMissing Values")

print(df.isnull().sum())

# ---------------------------------------------------------
# Dataset Summary
# ---------------------------------------------------------

print("\nCard Type Distribution")

print(df["card_type"].value_counts())

print("\nCard Network Distribution")

print(df["card_network"].value_counts())

print("\nCard Status Distribution")

print(df["card_status"].value_counts())

print("\nContactless Enabled")

print(df["contactless_enabled"].value_counts())

print("\nInternational Usage")

print(df["international_usage"].value_counts())

print("\nAverage Credit Limit")

print(round(df["credit_limit"].mean(), 2))

print("\nAverage Outstanding Balance")

print(round(df["outstanding_balance"].mean(), 2))

print("\nMaximum Credit Limit")

print(df["credit_limit"].max())

print("\nTotal Credit Limit")

print(df["credit_limit"].sum())

print("\nTotal Outstanding Balance")

print(round(df["outstanding_balance"].sum(), 2))

# ---------------------------------------------------------
# Output
# ---------------------------------------------------------

print("=" * 60)
print("Credit Cards Generated Successfully")
print("=" * 60)

print(df.head())

print(f"\nTotal Credit Cards : {len(df):,}")
print(f"Total Columns      : {len(df.columns)}")
print(f"Saved To           : {OUTPUT_PATH}")

print("=" * 60)