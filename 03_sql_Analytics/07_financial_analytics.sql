-- ------------------------------------------------------------------------------
-- SECTION 2: FINANCIAL OVERVIEW
-- ------------------------------------------------------------------------------


-- Q1. What is the total deposit balance across all customer accounts?
-- Purpose: Measure the total deposits maintained in active customer accounts.

SELECT
    SUM(current_balance) AS total_deposit_balance
FROM accounts
WHERE account_status = 'Active';


-- Q2. What is the total loan amount disbursed by the bank?
-- Purpose: Calculate the total loan amount issued to customers.

SELECT
    SUM(loan_amount) AS total_loan_amount_disbursed
FROM loans
WHERE loan_status = 'Active';


-- Q3. What is the total outstanding loan balance?
-- Purpose: Measure the bank's total outstanding loan exposure.

SELECT
    SUM(outstanding_balance) AS total_outstanding_loan_balance
FROM loans
WHERE loan_status = 'Active';


-- Q4. What is the total transaction value processed by the bank?
-- Purpose: Calculate the total value of all processed transactions.

SELECT
    SUM(transaction_amount) AS total_transaction_value
FROM transactions;


-- Q5. What is the total credit limit issued across all credit cards?
-- Purpose: Calculate the total credit limit provided to active credit card holders.

SELECT
    SUM(credit_limit) AS total_credit_limit
FROM credit_cards
WHERE card_status = 'Active';