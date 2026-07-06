USE banking_analytics;

-- ==============================================================================
-- PROJECT : Banking Analytics Platform
-- MODULE  : Deposit Analytics
-- FILE    : 02_deposit_analytics.sql
-- AUTHOR  : Kalpendra Yadav
-- DATE    : July 2026
-- DESCRIPTION : Analyze deposit accounts, balances, account performance,
--               and deposit portfolio metrics.
-- ==============================================================================


-- ------------------------------------------------------------------------------
-- SECTION 2: DEPOSIT OVERVIEW
-- ------------------------------------------------------------------------------


-- Q1. What is the total deposit balance across all customer accounts?
-- Purpose: Measure the total deposits held in active customer accounts.

SELECT
    SUM(current_balance) AS total_deposit_balance
FROM accounts
WHERE account_status = 'Active';


-- Q2. What is the average account balance?
-- Purpose: Calculate the average balance maintained in active accounts.

SELECT
    ROUND(AVG(current_balance), 2) AS average_account_balance
FROM accounts
WHERE account_status = 'Active';


-- Q3. How many deposit accounts are currently active?
-- Purpose: Count the total number of active deposit accounts.

SELECT
    COUNT(*) AS active_deposit_accounts
FROM accounts
WHERE account_status = 'Active';


-- Q4. Which account type has the highest number of active accounts?
-- Purpose: Identify the account type with the most active accounts.

SELECT
    account_type_id,
    COUNT(*) AS total_accounts
FROM accounts
WHERE account_status = 'Active'
GROUP BY account_type_id
ORDER BY total_accounts DESC
LIMIT 5;


-- Q5. Which account type holds the highest total deposits?
-- Purpose: Identify the account type contributing the highest deposit balance.

SELECT
    account_type_id,
    SUM(current_balance) AS total_deposit_balance
FROM accounts
WHERE account_status = 'Active'
GROUP BY account_type_id
ORDER BY total_deposit_balance DESC
LIMIT 5;