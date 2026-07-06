-- ==============================================================================
-- PROJECT : Banking Analytics Platform
-- MODULE  : Executive KPIs
-- FILE    : 09_executive_kpis.sql
-- AUTHOR  : Kalpendra Yadav
-- DATE    : July 2026
-- PURPOSE : Monitor key business metrics and executive-level KPIs to evaluate
--           the bank's overall financial performance and operational health.
-- ==============================================================================


-- ------------------------------------------------------------------------------
-- SECTION 1: EXECUTIVE KEY PERFORMANCE INDICATORS (KPIs)
-- ------------------------------------------------------------------------------


-- Q1. How many total customers does the bank serve?

-- Business Purpose: Calculate the total number of customers
--                  served by the bank.

SELECT
    COUNT(*) AS total_customers
FROM customers;


-- Q2. What is the total deposit balance across all customer accounts?

-- Business Purpose: Calculate the total deposit balance
--                  maintained across all active customer accounts.

SELECT
    SUM(current_balance) AS total_deposit_balance
FROM accounts
WHERE account_status = 'Active';


-- Q3. What is the total loan amount disbursed by the bank?

-- Business Purpose: Calculate the total loan amount
--                  disbursed to customers.

SELECT
    SUM(loan_amount) AS total_loan_amount_disbursed
FROM loans
WHERE loan_status = 'Active';


-- Q4. What is the total outstanding loan balance?

-- Business Purpose: Calculate the total outstanding loan balance
--                  to monitor the bank's credit exposure.

SELECT
    SUM(outstanding_balance) AS total_outstanding_loan_balance
FROM loans
WHERE loan_status = 'Active';


-- Q5. What is the total transaction value processed by the bank?

-- Business Purpose: Calculate the total value of financial
--                  transactions processed by the bank.

SELECT
    SUM(transaction_amount) AS total_transaction_value
FROM transactions;