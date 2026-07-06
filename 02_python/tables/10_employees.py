"""
==========================================================
Project     : Banking Analytics
File Name   : 13_employees.py
Description : Generate realistic employee data
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

NUM_BRANCHES = 100
TOTAL_EMPLOYEES = 2000

BANK_CODE = "BKAI"

# ---------------------------------------------------------
# Master Data
# ---------------------------------------------------------

DEPARTMENTS = [

    "Retail Banking",
    "Corporate Banking",
    "Loans",
    "Operations",
    "Customer Service",
    "Finance",
    "Risk Management",
    "Compliance",
    "Human Resources",
    "Information Technology"

]

DESIGNATIONS = [

    "Branch Manager",
    "Assistant Manager",
    "Relationship Manager",
    "Loan Officer",
    "Cashier",
    "Customer Service Executive",
    "Operations Executive",
    "Sales Executive",
    "Credit Analyst",
    "Clerk"

]

EMPLOYMENT_TYPES = [

    "Permanent",
    "Contract"

]

EMPLOYEE_STATUS = [

    "Active",
    "Inactive"

]

# ---------------------------------------------------------
# Helper Functions
# ---------------------------------------------------------

used_employee_codes = set()

def generate_employee_code():

    while True:

        code = (
            BANK_CODE +
            "EMP" +
            str(random.randint(100000,999999))
        )

        if code not in used_employee_codes:

            used_employee_codes.add(code)

            return code


def generate_joining_date():

    years = random.randint(0,20)

    joining_date = (
        datetime.today() -
        timedelta(days=365*years)
    )

    return joining_date.strftime("%Y-%m-%d")


def generate_dob():

    age = random.randint(21,60)

    dob = (
        datetime.today() -
        timedelta(days=365*age)
    )

    return dob.strftime("%Y-%m-%d")


def generate_salary(designation):

    salary_map = {

        "Branch Manager": (90000,180000),

        "Assistant Manager": (60000,90000),

        "Relationship Manager": (45000,80000),

        "Loan Officer": (35000,70000),

        "Cashier": (25000,45000),

        "Customer Service Executive": (25000,45000),

        "Operations Executive": (30000,55000),

        "Sales Executive": (30000,60000),

        "Credit Analyst": (50000,90000),

        "Clerk": (22000,35000)

    }

    low, high = salary_map[designation]

    return random.randint(low, high)

# ---------------------------------------------------------
# Employee List
# ---------------------------------------------------------

employees = []

employee_id = 1

# ---------------------------------------------------------
# Generate Employee Data
# ---------------------------------------------------------

for _ in range(TOTAL_EMPLOYEES):

    gender = random.choices(
        ["Male", "Female"],
        weights=[70, 30]
    )[0]

    if gender == "Male":
        first_name = fake.first_name_male()
    else:
        first_name = fake.first_name_female()

    last_name = fake.last_name()

    designation = random.choices(

        DESIGNATIONS,

        weights=[
            2,   # Branch Manager
            8,   # Assistant Manager
            12,  # Relationship Manager
            10,  # Loan Officer
            18,  # Cashier
            18,  # Customer Service Executive
            10,  # Operations Executive
            10,  # Sales Executive
            5,   # Credit Analyst
            7    # Clerk
        ]

    )[0]

    experience = random.randint(0, 35)

    employee = {

        "employee_id": employee_id,

        "employee_code": generate_employee_code(),

        "first_name": first_name,

        "last_name": last_name,

        "full_name": f"{first_name} {last_name}",

        "gender": gender,

        "date_of_birth": generate_dob(),

        "email": (
            f"{first_name.lower()}."
            f"{last_name.lower()}"
            f"{employee_id}@bankai.com"
        ),

        "phone_number": fake.msisdn()[:10],

        "branch_id": random.randint(1, NUM_BRANCHES),

        "department": random.choice(DEPARTMENTS),

        "designation": designation,

        "manager_id": (
            None
            if designation == "Branch Manager"
            else random.randint(1, employee_id)
        ),

        "joining_date": generate_joining_date(),

        "experience_years": experience,

        "salary": generate_salary(designation),

        "employment_type": random.choices(
            EMPLOYMENT_TYPES,
            weights=[92, 8]
        )[0],

        "performance_rating": round(
            random.uniform(2.5, 5.0),
            1
        ),

        "employee_status": random.choices(
            EMPLOYEE_STATUS,
            weights=[97, 3]
        )[0]

    }

    employees.append(employee)

    employee_id += 1

# ---------------------------------------------------------
# Create DataFrame
# ---------------------------------------------------------

df = pd.DataFrame(employees) 

# ---------------------------------------------------------
# Save CSV
# ---------------------------------------------------------

OUTPUT_PATH = "employees.csv"

df.to_csv(
    OUTPUT_PATH,
    index=False,
    encoding="utf-8"
)

# ---------------------------------------------------------
# Data Validation
# ---------------------------------------------------------

print("\nChecking Data Quality...\n")

print(f"Duplicate Employee IDs      : {df['employee_id'].duplicated().sum()}")
print(f"Duplicate Employee Codes    : {df['employee_code'].duplicated().sum()}")
print(f"Duplicate Emails           : {df['email'].duplicated().sum()}")

print("\nMissing Values")

print(df.isnull().sum())

# ---------------------------------------------------------
# Dataset Summary
# ---------------------------------------------------------

print("\nDepartment Distribution")

print(df["department"].value_counts())

print("\nDesignation Distribution")

print(df["designation"].value_counts())

print("\nEmployment Type")

print(df["employment_type"].value_counts())

print("\nEmployee Status")

print(df["employee_status"].value_counts())

print("\nGender Distribution")

print(df["gender"].value_counts())

print("\nAverage Salary")

print(round(df["salary"].mean(), 2))

print("\nMaximum Salary")

print(df["salary"].max())

print("\nMinimum Salary")

print(df["salary"].min())

print("\nAverage Experience")

print(round(df["experience_years"].mean(), 2))

print("\nAverage Performance Rating")

print(round(df["performance_rating"].mean(), 2))

print("\nEmployees Per Branch")

print(round(len(df) / NUM_BRANCHES, 2))

# ---------------------------------------------------------
# Output
# ---------------------------------------------------------

print("=" * 60)
print("Employees Generated Successfully")
print("=" * 60)

print(df.head())

print(f"\nTotal Employees : {len(df):,}")
print(f"Total Columns   : {len(df.columns)}")
print(f"Saved To        : {OUTPUT_PATH}")

print("=" * 60)