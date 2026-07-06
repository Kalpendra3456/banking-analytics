"""
==========================================================
Project     : Banking Analytics
File Name   : 01_branches.py
Description : Generate realistic bank branch data
Author      : Kalpendra Yadav
==========================================================
"""

import random
import pandas as pd
from faker import Faker

# ---------------------------------------------------------
# Configuration
# ---------------------------------------------------------

fake = Faker("en_IN")

random.seed(42)
Faker.seed(42)

NUM_BRANCHES = 100

BANK_CODE = "BKAI"

# ---------------------------------------------------------
# Cities & States
# ---------------------------------------------------------

LOCATIONS = [
    ("Mumbai", "Maharashtra"),
    ("Pune", "Maharashtra"),
    ("Nagpur", "Maharashtra"),
    ("Delhi", "Delhi"),
    ("Noida", "Uttar Pradesh"),
    ("Ghaziabad", "Uttar Pradesh"),
    ("Lucknow", "Uttar Pradesh"),
    ("Kanpur", "Uttar Pradesh"),
    ("Agra", "Uttar Pradesh"),
    ("Varanasi", "Uttar Pradesh"),
    ("Jaipur", "Rajasthan"),
    ("Udaipur", "Rajasthan"),
    ("Kota", "Rajasthan"),
    ("Ahmedabad", "Gujarat"),
    ("Surat", "Gujarat"),
    ("Vadodara", "Gujarat"),
    ("Bengaluru", "Karnataka"),
    ("Mysuru", "Karnataka"),
    ("Hyderabad", "Telangana"),
    ("Warangal", "Telangana"),
    ("Chennai", "Tamil Nadu"),
    ("Coimbatore", "Tamil Nadu"),
    ("Madurai", "Tamil Nadu"),
    ("Kochi", "Kerala"),
    ("Thiruvananthapuram", "Kerala"),
    ("Kolkata", "West Bengal"),
    ("Howrah", "West Bengal"),
    ("Bhubaneswar", "Odisha"),
    ("Patna", "Bihar"),
    ("Ranchi", "Jharkhand"),
    ("Bhopal", "Madhya Pradesh"),
    ("Indore", "Madhya Pradesh"),
    ("Raipur", "Chhattisgarh"),
    ("Chandigarh", "Chandigarh"),
    ("Amritsar", "Punjab"),
    ("Ludhiana", "Punjab"),
    ("Dehradun", "Uttarakhand"),
    ("Shimla", "Himachal Pradesh"),
    ("Guwahati", "Assam"),
    ("Srinagar", "Jammu & Kashmir")
]

# ---------------------------------------------------------
# Branch Types
# ---------------------------------------------------------

BRANCH_TYPES = [
    "Retail",
    "Corporate",
    "Rural",
    "Urban",
    "Semi Urban"
]

# ---------------------------------------------------------
# Generate Data
# ---------------------------------------------------------

branches = []

used_ifsc = set()

for i in range(1, NUM_BRANCHES + 1):

    city, state = random.choice(LOCATIONS)

    branch_id = i

    branch_code = f"BR{i:04d}"

    while True:
        ifsc = BANK_CODE + str(random.randint(100000, 999999))
        if ifsc not in used_ifsc:
            used_ifsc.add(ifsc)
            break

    branch = {

        "branch_id": branch_id,

        "branch_code": branch_code,

        "branch_name": f"{city} Branch",

        "branch_type": random.choice(BRANCH_TYPES),

        "ifsc_code": ifsc,

        "address": fake.street_address(),

        "city": city,

        "state": state,

        "postal_code": fake.postcode(),

        "country": "India",

        "phone_number": fake.msisdn()[:10],

        "email": f"{city.lower().replace(' ','')}{i}@bankai.com",

        "manager_name": fake.name(),

        "opening_year": random.randint(1995, 2024),

        "number_of_employees": random.randint(8, 40),

        "status": random.choices(
            ["Active", "Inactive"],
            weights=[98, 2]
        )[0]

    }

    branches.append(branch)

# ---------------------------------------------------------
# DataFrame
# ---------------------------------------------------------

df = pd.DataFrame(branches)

# ---------------------------------------------------------
# Save CSV
# ---------------------------------------------------------

# ---------------------------------------------------------
# Save CSV
# ---------------------------------------------------------

OUTPUT_PATH = "branches.csv"

df.to_csv(
    OUTPUT_PATH,
    index=False,
    encoding="utf-8-sig"
)

print("=" * 60)
print("Branches Generated Successfully")
print("=" * 60)
print(df.head())
print(f"\nTotal Branches : {len(df):,}")
print(f"Saved To       : {OUTPUT_PATH}")