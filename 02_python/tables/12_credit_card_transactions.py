"""
==========================================================
Project     : Banking Analytics
File Name   : 11_credit_card_transactions.py
Description : Generate realistic credit card transactions
Author      : Kalpendra Yadav
==========================================================
"""

import random
from datetime import datetime, timedelta

import pandas as pd
from faker import Faker

# ---------------------------------------------------------
# Configuration
# ---------------------------------------------------------

fake = Faker("en_IN")

random.seed(42)
Faker.seed(42)

NUM_CARDS = 4500
TRANSACTIONS_PER_CARD = random.randint(40, 80)

# ---------------------------------------------------------
# Master Data
# ---------------------------------------------------------

MERCHANT_CATEGORIES = {

    "Grocery": [
        "DMart",
        "Reliance Fresh",
        "Big Bazaar",
        "More Supermarket"
    ],

    "Fuel": [
        "Indian Oil",
        "HP Petrol Pump",
        "BPCL",
        "Shell"
    ],

    "Restaurant": [
        "McDonald's",
        "Domino's",
        "KFC",
        "Pizza Hut",
        "Haldiram's"
    ],

    "Shopping": [
        "Amazon",
        "Flipkart",
        "Myntra",
        "Reliance Trends"
    ],

    "Travel": [
        "IRCTC",
        "MakeMyTrip",
        "Goibibo",
        "Uber",
        "Ola"
    ],

    "Hotel": [
        "Taj Hotels",
        "ITC Hotels",
        "OYO",
        "FabHotels"
    ],

    "Healthcare": [
        "Apollo Pharmacy",
        "Fortis",
        "Max Hospital",
        "MedPlus"
    ],

    "Entertainment": [
        "PVR",
        "INOX",
        "Netflix",
        "BookMyShow"
    ],

    "Education": [
        "Udemy",
        "Coursera",
        "Unacademy",
        "BYJU'S"
    ],

    "Utility Bills": [
        "Electricity Board",
        "Jio Fiber",
        "Airtel",
        "BSNL"
    ],

    "Electronics": [
        "Croma",
        "Vijay Sales",
        "Samsung Store",
        "Apple Store"
    ],

    "Insurance": [
        "LIC",
        "HDFC Life",
        "ICICI Lombard",
        "Star Health"
    ]
}

PAYMENT_MODES = [
    "Chip",
    "Tap",
    "Swipe",
    "Online"
]

TRANSACTION_STATUS = [
    "Success",
    "Failed",
    "Reversed"
]

CITIES = [
    "Mumbai",
    "Delhi",
    "Bengaluru",
    "Hyderabad",
    "Chennai",
    "Kolkata",
    "Pune",
    "Ahmedabad",
    "Lucknow",
    "Jaipur",
    "Noida",
    "Ghaziabad"
]

STATES = [
    "Maharashtra",
    "Delhi",
    "Karnataka",
    "Telangana",
    "Tamil Nadu",
    "West Bengal",
    "Gujarat",
    "Uttar Pradesh",
    "Rajasthan"
]

# ---------------------------------------------------------
# Helper Functions
# ---------------------------------------------------------

def generate_transaction_datetime():

    days = random.randint(0, 730)

    seconds = random.randint(0, 86399)

    transaction_time = (
        datetime.now()
        - timedelta(days=days, seconds=seconds)
    )

    return transaction_time.strftime("%Y-%m-%d %H:%M:%S")


def generate_amount():

    return round(

        random.choices(

            [
                random.uniform(50,500),
                random.uniform(500,3000),
                random.uniform(3000,10000),
                random.uniform(10000,50000)
            ],

            weights=[40,35,20,5]

        )[0],

        2

    )


def generate_reward_points(amount):

    return int(amount // 100)


# ---------------------------------------------------------
# Transaction List
# ---------------------------------------------------------

transactions = []

transaction_id = 1 

# ---------------------------------------------------------
# Generate Credit Card Transactions
# ---------------------------------------------------------

for card_id in range(1, NUM_CARDS + 1):

    transaction_count = random.randint(40, 80)

    for _ in range(transaction_count):

        category = random.choice(
            list(MERCHANT_CATEGORIES.keys())
        )

        merchant = random.choice(
            MERCHANT_CATEGORIES[category]
        )

        amount = generate_amount()

        city = random.choice(CITIES)

        if city in ["Mumbai", "Pune"]:
            state = "Maharashtra"

        elif city == "Delhi":
            state = "Delhi"

        elif city == "Bengaluru":
            state = "Karnataka"

        elif city == "Hyderabad":
            state = "Telangana"

        elif city == "Chennai":
            state = "Tamil Nadu"

        elif city == "Kolkata":
            state = "West Bengal"

        elif city == "Ahmedabad":
            state = "Gujarat"

        elif city in ["Lucknow", "Noida", "Ghaziabad"]:
            state = "Uttar Pradesh"

        elif city == "Jaipur":
            state = "Rajasthan"

        else:
            state = random.choice(STATES)

        international = random.choices(
            ["Yes", "No"],
            weights=[3, 97]
        )[0]

        fraud = random.choices(
            ["Yes", "No"],
            weights=[1, 999]
        )[0]

        transaction = {

            "transaction_id": transaction_id,

            "card_id": card_id,

            "transaction_datetime":
                generate_transaction_datetime(),

            "merchant_name": merchant,

            "merchant_category": category,

            "city": city,

            "state": state,

            "transaction_amount": amount,

            "currency": "INR",

            "payment_mode": random.choices(
                PAYMENT_MODES,
                weights=[30,25,20,25]
            )[0],

            "transaction_status": random.choices(
                TRANSACTION_STATUS,
                weights=[97,2,1]
            )[0],

            "reward_points":
                generate_reward_points(amount),

            "international_transaction":
                international,

            "fraud_flag":
                fraud

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

OUTPUT_PATH = "credit_card_transactions.csv"

df.to_csv(
    OUTPUT_PATH,
    index=False,
    encoding="utf-8-sig"
)

# ---------------------------------------------------------
# Data Validation
# ---------------------------------------------------------

print("\nChecking Data Quality...\n")

print(f"Duplicate Transaction IDs : {df['transaction_id'].duplicated().sum()}")

print("\nMissing Values")

print(df.isnull().sum())

# ---------------------------------------------------------
# Dataset Summary
# ---------------------------------------------------------

print("\nTransaction Status")

print(df["transaction_status"].value_counts())

print("\nMerchant Categories")

print(df["merchant_category"].value_counts())

print("\nPayment Modes")

print(df["payment_mode"].value_counts())

print("\nInternational Transactions")

print(df["international_transaction"].value_counts())

print("\nFraud Transactions")

print(df["fraud_flag"].value_counts())

print("\nTop 10 Merchants")

print(df["merchant_name"].value_counts().head(10))

print("\nAverage Transaction Amount")

print(round(df["transaction_amount"].mean(), 2))

print("\nMaximum Transaction Amount")

print(round(df["transaction_amount"].max(), 2))

print("\nMinimum Transaction Amount")

print(round(df["transaction_amount"].min(), 2))

print("\nTotal Transaction Amount")

print(round(df["transaction_amount"].sum(), 2))

# ---------------------------------------------------------
# Output
# ---------------------------------------------------------

print("=" * 60)
print("Credit Card Transactions Generated Successfully")
print("=" * 60)

print(df.head())

print(f"\nTotal Transactions : {len(df):,}")
print(f"Total Columns      : {len(df.columns)}")
print(f"Saved To           : {OUTPUT_PATH}")

print("=" * 60)