USE banking_analytics;

-- ==============================================================================
-- PROJECT : Banking Analytics Platform
-- MODULE  : Transaction Analytics
-- FILE    : 04_transaction_analytics.sql
-- AUTHOR  : Kalpendra Yadav
-- DATE    : July 2026
-- DESCRIPTION : Analyze transaction volume, value, and performance across
--               different transaction types.
-- ==============================================================================


-- ------------------------------------------------------------------------------
-- SECTION 2: TRANSACTION OVERVIEW
-- ------------------------------------------------------------------------------


-- Q1. How many transactions have been processed by the bank?
-- Purpose: Count the total number of transactions.

SELECT
    COUNT(*) AS total_transactions
FROM transactions;


-- Q2. What is the total transaction amount?
-- Purpose: Measure the total value of all transactions.

SELECT
    SUM(transaction_amount) AS total_transaction_amount
FROM transactions;


-- Q3. What is the average transaction amount?
-- Purpose: Calculate the average transaction value.

SELECT
    ROUND(AVG(transaction_amount), 2) AS average_transaction_amount
FROM transactions;


-- Q4. Which transaction type has the highest transaction volume?
-- Purpose: Identify the transaction type with the highest transaction count.

SELECT
    transaction_type_id,
    COUNT(*) AS total_transactions
FROM transactions
GROUP BY transaction_type_id
ORDER BY total_transactions DESC
LIMIT 1;


-- Q5. Which transaction type has the highest total transaction amount?
-- Purpose: Identify the transaction type contributing the highest transaction value.

SELECT
    transaction_type_id,
    SUM(transaction_amount) AS total_transaction_amount
FROM transactions
GROUP BY transaction_type_id
ORDER BY total_transaction_amount DESC
LIMIT 1;