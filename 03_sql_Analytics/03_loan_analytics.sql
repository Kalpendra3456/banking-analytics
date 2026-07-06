USE banking_analytics;

-- ==============================================================================
-- PROJECT : Banking Analytics Platform
-- MODULE  : Loan Analytics
-- FILE    : 03_loan_analytics.sql
-- AUTHOR  : Kalpendra Yadav
-- DATE    : July 2026
-- DESCRIPTION : Analyze loan portfolio performance, lending trends, and key
--               loan metrics.
-- ==============================================================================


-- ------------------------------------------------------------------------------
-- SECTION 2: LOAN PORTFOLIO OVERVIEW
-- ------------------------------------------------------------------------------


-- Q1. What is the total loan amount disbursed by the bank?
-- Purpose: Measure the total loan amount issued to customers.

SELECT
    SUM(loan_amount) AS total_loan_amount_disbursed
FROM loans;


-- Q2. What is the average loan amount issued?
-- Purpose: Calculate the average loan amount across all loans.

SELECT
    ROUND(AVG(loan_amount), 2) AS average_loan_amount
FROM loans;


-- Q3. How many loans are currently active?
-- Purpose: Count the total number of active loans.

SELECT
    COUNT(*) AS active_loans
FROM loans
WHERE loan_status = 'Active';


-- Q4. What is the total outstanding loan balance?
-- Purpose: Measure the bank's outstanding loan exposure.

SELECT
    SUM(outstanding_balance) AS total_outstanding_loan_balance
FROM loans
WHERE loan_status = 'Active';


-- Q5. Which loan type has the highest total loan amount?
-- Purpose: Identify the loan purpose contributing the highest loan amount.

SELECT
    purpose,
    SUM(loan_amount) AS total_loan_amount
FROM loans
GROUP BY purpose
ORDER BY total_loan_amount DESC
LIMIT 5;