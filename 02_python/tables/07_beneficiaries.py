"""
==========================================================
Project     : Banking Analytics
File Name   : 07_beneficiaries.py
Description : Generate realistic beneficiary data
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

# Total Accounts (Generated from accounts.py)
NUM_ACCOUNTS = 20000

BANK_CODE = "BKAI"

# ---------------------------------------------------------
# Master Data
# ---------------------------------------------------------

BANKS = [
    "State Bank of India",
    "HDFC Bank",
    "ICICI Bank",
    "Axis Bank",
    "Punjab National Bank",
    "Bank of Baroda",
    "Canara Bank",
    "Union Bank of India",
    "Indian Bank",
    "Kotak Mahindra Bank",
    "IndusInd Bank",
    "IDFC FIRST Bank",
    "Yes Bank",
    "AU Small Finance Bank",
    "Bandhan Bank"
]

RELATIONSHIPS = [
    "Self",
    "Father",
    "Mother",
    "Brother",
    "Sister",
    "Spouse",
    "Friend",
    "Business Partner",
    "Employer",
    "Employee",
    "Other"
]

BENEFICIARY_TYPES = [
    "Internal",
    "External"
]

STATUS = [
    "Active",
    "Inactive"
]

# ---------------------------------------------------------
# Helper Functions
# ---------------------------------------------------------

used_account_numbers = set()
used_codes = set()

def generate_beneficiary_code():

    while True:

        code = "BEN" + str(random.randint(100000,999999))

        if code not in used_codes:
            used_codes.add(code)
            return code


def generate_account_number():

    while True:

        number = str(random.randint(
            100000000000,
            999999999999
        ))

        if number not in used_account_numbers:
            used_account_numbers.add(number)
            return number


def generate_ifsc():

    return (
        BANK_CODE +
        str(random.randint(100000,999999))
    )


def generate_added_date():

    days = random.randint(30,3650)

    return (
        datetime.today() -
        timedelta(days=days)
    ).strftime("%Y-%m-%d")

# ---------------------------------------------------------
# Beneficiary List
# ---------------------------------------------------------

beneficiaries = []

beneficiary_id = 1

# ---------------------------------------------------------
# Generate Beneficiaries
# ---------------------------------------------------------

for account_id in range(1, NUM_ACCOUNTS + 1):

    # Each account has 0–4 beneficiaries
    total_beneficiaries = random.choices(
        [0, 1, 2, 3, 4],
        weights=[10, 30, 35, 20, 5]
    )[0]

    for _ in range(total_beneficiaries):

        beneficiary_type = random.choices(
            BENEFICIARY_TYPES,
            weights=[30, 70]          # Internal / External
        )[0]

        bank_name = (
            "BankAI"
            if beneficiary_type == "Internal"
            else random.choice(BANKS)
        )

        gender = random.choice(["Male", "Female"])

        if gender == "Male":
            beneficiary_name = fake.name_male()
        else:
            beneficiary_name = fake.name_female()

        city = fake.city()
        state = fake.state()

        beneficiary = {

            "beneficiary_id": beneficiary_id,

            "beneficiary_code": generate_beneficiary_code(),

            "account_id": account_id,

            "beneficiary_name": beneficiary_name,

            "beneficiary_bank": bank_name,

            "beneficiary_account_number": generate_account_number(),

            "ifsc_code": generate_ifsc(),

            "relationship": random.choices(
                RELATIONSHIPS,
                weights=[15,10,10,8,8,15,20,5,3,3,3]
            )[0],

            "beneficiary_type": beneficiary_type,

            "city": city,

            "state": state,

            "mobile_number": fake.msisdn()[:10],

            "email": (
                beneficiary_name.lower()
                .replace(" ", ".")
                + "@gmail.com"
            ),

            "added_date": generate_added_date(),

            "status": random.choices(
                STATUS,
                weights=[98,2]
            )[0]

        }

        beneficiaries.append(beneficiary)

        beneficiary_id += 1

# ---------------------------------------------------------
# Create DataFrame
# ---------------------------------------------------------

df = pd.DataFrame(beneficiaries) 

# ---------------------------------------------------------
# Save CSV
# ---------------------------------------------------------

OUTPUT_PATH = "beneficiaries.csv"

df.to_csv(
    OUTPUT_PATH,
    index=False,
    encoding="utf-8-sig"
)

# ---------------------------------------------------------
# Data Validation
# ---------------------------------------------------------

print("\nChecking Data Quality...\n")

print(f"Duplicate Beneficiary IDs      : {df['beneficiary_id'].duplicated().sum()}")
print(f"Duplicate Beneficiary Codes    : {df['beneficiary_code'].duplicated().sum()}")
print(f"Duplicate Account Numbers      : {df['beneficiary_account_number'].duplicated().sum()}")

print("\nMissing Values")

print(df.isnull().sum())

# ---------------------------------------------------------
# Dataset Summary
# ---------------------------------------------------------

print("\nBeneficiary Type")

print(df["beneficiary_type"].value_counts())

print("\nRelationship")

print(df["relationship"].value_counts())

print("\nStatus")

print(df["status"].value_counts())

print("\nTop Banks")

print(df["beneficiary_bank"].value_counts().head(10))

print("\nTop States")

print(df["state"].value_counts().head(10))

# ---------------------------------------------------------
# Output
# ---------------------------------------------------------

print("=" * 60)
print("Beneficiaries Generated Successfully")
print("=" * 60)

print(df.head())

print(f"\nTotal Beneficiaries : {len(df):,}")
print(f"Total Columns       : {len(df.columns)}")
print(f"Saved To            : {OUTPUT_PATH}")

print("=" * 60)