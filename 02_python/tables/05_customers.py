"""
==========================================================
Project     : Banking Analytics
File Name   : 05_customers.py
Description : Generate realistic customer master data
Author      : Kalpendra Yadav
==========================================================
"""

import csv
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

NUM_CUSTOMERS = 10000

# ---------------------------------------------------------
# Master Data
# ---------------------------------------------------------

GENDERS = ["Male", "Female", "Other"]

MARITAL_STATUS = [
    "Single",
    "Married",
    "Divorced"
]

CUSTOMER_STATUS = [
    "Active",
    "Inactive"
]

KYC_STATUS = [
    "Verified",
    "Pending"
]

RISK_CATEGORY = [
    "Low",
    "Medium",
    "High"
]

OCCUPATIONS = [
    "Software Engineer",
    "Doctor",
    "Teacher",
    "Business Owner",
    "Accountant",
    "Farmer",
    "Government Employee",
    "Civil Engineer",
    "Mechanical Engineer",
    "Lawyer",
    "Nurse",
    "Police Officer",
    "Sales Executive",
    "Marketing Manager",
    "HR Manager",
    "Electrician",
    "Driver",
    "Shopkeeper",
    "Student",
    "Retired"
]

LOCATIONS = [
    ("Mumbai","Maharashtra"),
    ("Pune","Maharashtra"),
    ("Nagpur","Maharashtra"),
    ("Delhi","Delhi"),
    ("Noida","Uttar Pradesh"),
    ("Ghaziabad","Uttar Pradesh"),
    ("Lucknow","Uttar Pradesh"),
    ("Kanpur","Uttar Pradesh"),
    ("Agra","Uttar Pradesh"),
    ("Varanasi","Uttar Pradesh"),
    ("Jaipur","Rajasthan"),
    ("Udaipur","Rajasthan"),
    ("Ahmedabad","Gujarat"),
    ("Surat","Gujarat"),
    ("Vadodara","Gujarat"),
    ("Bengaluru","Karnataka"),
    ("Mysuru","Karnataka"),
    ("Hyderabad","Telangana"),
    ("Warangal","Telangana"),
    ("Chennai","Tamil Nadu"),
    ("Coimbatore","Tamil Nadu"),
    ("Madurai","Tamil Nadu"),
    ("Kochi","Kerala"),
    ("Thiruvananthapuram","Kerala"),
    ("Kolkata","West Bengal"),
    ("Howrah","West Bengal"),
    ("Bhubaneswar","Odisha"),
    ("Patna","Bihar"),
    ("Ranchi","Jharkhand"),
    ("Bhopal","Madhya Pradesh"),
    ("Indore","Madhya Pradesh"),
    ("Raipur","Chhattisgarh"),
    ("Chandigarh","Chandigarh"),
    ("Amritsar","Punjab"),
    ("Ludhiana","Punjab"),
    ("Dehradun","Uttarakhand"),
    ("Shimla","Himachal Pradesh"),
    ("Guwahati","Assam"),
    ("Srinagar","Jammu & Kashmir")
]

# ---------------------------------------------------------
# Unique Values
# ---------------------------------------------------------

used_pan = set()
used_aadhaar = set()
used_phone = set()

# ---------------------------------------------------------
# Helper Functions
# ---------------------------------------------------------

def generate_pan():
    """Generate unique PAN number"""

    while True:

        pan = (
            "".join(random.choices(string.ascii_uppercase, k=5))
            + str(random.randint(1000, 9999))
            + random.choice(string.ascii_uppercase)
        )

        if pan not in used_pan:
            used_pan.add(pan)
            return pan


def generate_aadhaar():
    """Generate unique Aadhaar"""

    while True:

        aadhaar = "".join(random.choices("0123456789", k=12))

        if aadhaar not in used_aadhaar:
            used_aadhaar.add(aadhaar)
            return aadhaar


def generate_phone():
    """Generate unique mobile number"""

    while True:

        phone = random.choice(
            ["98", "99", "97", "96", "95", "94", "93", "91"]
        ) + "".join(random.choices("0123456789", k=8))

        if phone not in used_phone:
            used_phone.add(phone)
            return phone


def generate_income():
    """Weighted annual income"""

    return random.choices(

        [
            random.randint(200000, 500000),
            random.randint(500001, 1000000),
            random.randint(1000001, 2000000),
            random.randint(2000001, 5000000),
            random.randint(5000001, 10000000)
        ],

        weights=[35, 30, 20, 10, 5]

    )[0]


def generate_dob():

    age = random.randint(18, 80)

    dob = datetime.today() - timedelta(days=age * 365)

    return dob.strftime("%Y-%m-%d")


def generate_customer_since():

    years = random.randint(0, 15)

    joined = datetime.today() - timedelta(days=years * 365)

    return joined.strftime("%Y-%m-%d")


# ---------------------------------------------------------
# Customer List
# ---------------------------------------------------------

customers = []
# ---------------------------------------------------------
# Generate Customer Data
# ---------------------------------------------------------

for i in range(1, NUM_CUSTOMERS + 1):

    gender = random.choices(
        GENDERS,
        weights=[54, 45, 1]
    )[0]

    if gender == "Male":
        first_name = fake.first_name_male()

    elif gender == "Female":
        first_name = fake.first_name_female()

    else:
        first_name = fake.first_name()

    last_name = fake.last_name()

    city, state = random.choice(LOCATIONS)

    customer = {

        "customer_id": i,

        "customer_code": f"CUST{i:06d}",

        "first_name": first_name,

        "last_name": last_name,

        "full_name": f"{first_name} {last_name}",

        "gender": gender,

        "date_of_birth": generate_dob(),

        "marital_status": random.choices(
            MARITAL_STATUS,
            weights=[35, 60, 5]
        )[0],

        "occupation": random.choice(OCCUPATIONS),

        "annual_income": generate_income(),

        "phone_number": generate_phone(),

        "email": (
            f"{first_name.lower()}."
            f"{last_name.lower()}"
            f"{random.randint(10,999)}@gmail.com"
        ),

        "address": fake.street_address(),

        "city": city,

        "state": state,

        "postal_code": fake.postcode(),

        "country": "India",

        "pan_number": generate_pan(),

        "aadhaar_number": generate_aadhaar(),

        "customer_since": generate_customer_since(),

        "risk_category": random.choices(
            RISK_CATEGORY,
            weights=[70,22,8]
        )[0],

        "kyc_status": random.choices(
            KYC_STATUS,
            weights=[95,5]
        )[0],

        "customer_status": random.choices(
            CUSTOMER_STATUS,
            weights=[96,4]
        )[0]

    }

    customers.append(customer)

# ---------------------------------------------------------
# Create DataFrame
# ---------------------------------------------------------

df = pd.DataFrame(customers)

# ---------------------------------------------------------
# Save CSV
# ---------------------------------------------------------

OUTPUT_PATH = "customers.csv"

df.to_csv(
    "customers.csv",
    index=False,
    quoting=csv.QUOTE_ALL
)

# ---------------------------------------------------------
# Data Validation
# ---------------------------------------------------------

print("\nChecking Data Quality...")

print(f"Duplicate Customer IDs   : {df['customer_id'].duplicated().sum()}")
print(f"Duplicate Customer Codes : {df['customer_code'].duplicated().sum()}")
print(f"Duplicate PAN Numbers    : {df['pan_number'].duplicated().sum()}")
print(f"Duplicate Aadhaar        : {df['aadhaar_number'].duplicated().sum()}")
print(f"Duplicate Phone Numbers  : {df['phone_number'].duplicated().sum()}")

print("\nMissing Values")

print(df.isnull().sum())

# ---------------------------------------------------------
# Dataset Summary
# ---------------------------------------------------------

print("\nCustomer Status")

print(df["customer_status"].value_counts())

print("\nGender Distribution")

print(df["gender"].value_counts())

print("\nRisk Category")

print(df["risk_category"].value_counts())

print("\nKYC Status")

print(df["kyc_status"].value_counts())

print("\nTop 10 Occupations")

print(df["occupation"].value_counts().head(10))

print("\nTop 10 States")

print(df["state"].value_counts().head(10))

# ---------------------------------------------------------
# Output
# ---------------------------------------------------------

print("=" * 60)
print("Customers Generated Successfully")
print("=" * 60)

print(df.head())

print(f"\nTotal Customers : {len(df):,}")
print(f"Total Columns   : {len(df.columns)}")
print(f"Saved To        : {OUTPUT_PATH}")

print("=" * 60)