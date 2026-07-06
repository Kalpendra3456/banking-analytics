-- ------------------------------------------------------------------------------
-- SECTION 2: RISK OVERVIEW
-- ------------------------------------------------------------------------------


-- Q1. How many customers belong to each risk category?
-- Purpose: Analyze the distribution of customers across risk categories.

SELECT
    risk_category,
    COUNT(*) AS total_customers
FROM customers
GROUP BY risk_category
ORDER BY total_customers DESC;


-- Q2. How many transactions have been flagged as fraudulent?
-- Purpose: Count the total number of fraudulent transactions.

SELECT
    COUNT(*) AS fraudulent_transactions
FROM transactions
WHERE fraud_flag = 'Yes';


-- Q3. How many active loans are overdue?
-- Purpose: Identify the total number of active overdue loans.

SELECT
    COUNT(*) AS overdue_active_loans
FROM loans
WHERE loan_status = 'Active'
  AND repayment_status = 'Overdue';


-- Q4. How many customer accounts are currently blocked or frozen?
-- Purpose: Measure the total number of blocked or frozen accounts.

SELECT
    COUNT(*) AS blocked_or_frozen_accounts
FROM accounts
WHERE account_status IN ('Blocked', 'Frozen');


-- Q5. Which account type has the highest number of blocked accounts?
-- Purpose: Identify the account type with the most blocked accounts.

SELECT
    account_type_id,
    COUNT(*) AS blocked_accounts
FROM accounts
WHERE account_status = 'Blocked'
GROUP BY account_type_id
ORDER BY blocked_accounts DESC
LIMIT 1;