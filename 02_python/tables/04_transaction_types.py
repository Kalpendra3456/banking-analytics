"""
==========================================================
Project     : Banking Analytics
File Name   : 04_transaction_types.py
Description : Generate transaction types master data
Author      : Kalpendra Yadav
==========================================================
"""

import pandas as pd

# ---------------------------------------------------------
# Transaction Types Master Data
# ---------------------------------------------------------

transaction_types = [
    {
        "transaction_type_id": 1,
        "transaction_type": "Cash Deposit",
        "category": "Deposit",
        "channel": "Branch",
        "status": "Active"
    },
    {
        "transaction_type_id": 2,
        "transaction_type": "Cash Withdrawal",
        "category": "Withdrawal",
        "channel": "ATM",
        "status": "Active"
    },
    {
        "transaction_type_id": 3,
        "transaction_type": "Online Transfer",
        "category": "Transfer",
        "channel": "Internet Banking",
        "status": "Active"
    },
    {
        "transaction_type_id": 4,
        "transaction_type": "NEFT",
        "category": "Transfer",
        "channel": "Online",
        "status": "Active"
    },
    {
        "transaction_type_id": 5,
        "transaction_type": "RTGS",
        "category": "Transfer",
        "channel": "Online",
        "status": "Active"
    },
    {
        "transaction_type_id": 6,
        "transaction_type": "IMPS",
        "category": "Transfer",
        "channel": "Mobile Banking",
        "status": "Active"
    },
    {
        "transaction_type_id": 7,
        "transaction_type": "UPI Payment",
        "category": "Payment",
        "channel": "UPI",
        "status": "Active"
    },
    {
        "transaction_type_id": 8,
        "transaction_type": "Debit Card Purchase",
        "category": "Purchase",
        "channel": "POS",
        "status": "Active"
    },
    {
        "transaction_type_id": 9,
        "transaction_type": "Credit Card Payment",
        "category": "Payment",
        "channel": "Online",
        "status": "Active"
    },
    {
        "transaction_type_id": 10,
        "transaction_type": "Cheque Deposit",
        "category": "Deposit",
        "channel": "Branch",
        "status": "Active"
    },
    {
        "transaction_type_id": 11,
        "transaction_type": "Cheque Withdrawal",
        "category": "Withdrawal",
        "channel": "Branch",
        "status": "Active"
    },
    {
        "transaction_type_id": 12,
        "transaction_type": "Loan EMI Payment",
        "category": "Loan",
        "channel": "Auto Debit",
        "status": "Active"
    },
    {
        "transaction_type_id": 13,
        "transaction_type": "Interest Credit",
        "category": "Interest",
        "channel": "System",
        "status": "Active"
    },
    {
        "transaction_type_id": 14,
        "transaction_type": "Service Charge",
        "category": "Charges",
        "channel": "System",
        "status": "Active"
    },
    {
        "transaction_type_id": 15,
        "transaction_type": "Refund",
        "category": "Refund",
        "channel": "Online",
        "status": "Active"
    }
]

# ---------------------------------------------------------
# Create DataFrame
# ---------------------------------------------------------

df = pd.DataFrame(transaction_types)

# ---------------------------------------------------------
# Save CSV
# ---------------------------------------------------------

OUTPUT_PATH = "transaction_types.csv"

df.to_csv(
    OUTPUT_PATH,
    index=False,
    encoding="utf-8-sig"
)

# ---------------------------------------------------------
# Output
# ---------------------------------------------------------

from pathlib import Path

print(f"Saved To                : {Path(OUTPUT_PATH).resolve()}")