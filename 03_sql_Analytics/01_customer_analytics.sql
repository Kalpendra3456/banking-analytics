-- ------------------------------------------------------------------------------
-- SECTION 1: CUSTOMER OVERVIEW
-- ------------------------------------------------------------------------------


-- Q1. How many customers are registered?
-- Purpose: Count the total number of registered customers.

SELECT
    COUNT(*) AS total_customers
FROM customers;


-- Q2. Which city has the highest number of customers?
-- Purpose: Identify the city with the largest customer base.

SELECT
    city,
    COUNT(*) AS total_customers
FROM customers
GROUP BY city
ORDER BY total_customers DESC
LIMIT 5;


-- Q3. Which state has the highest number of customers?
-- Purpose: Analyze customer distribution across states.

SELECT
    state,
    COUNT(*) AS total_customers
FROM customers
GROUP BY state
ORDER BY total_customers DESC
LIMIT 5;


-- Q4. How many customers belong to each risk category?
-- Purpose: Analyze the distribution of customers by risk level.

SELECT
    risk_category,
    COUNT(*) AS total_customers
FROM customers
GROUP BY risk_category
ORDER BY total_customers DESC;


-- Q5. How many customers have completed KYC verification?
-- Purpose: Measure customer KYC compliance.

SELECT
    kyc_status,
    COUNT(*) AS total_customers
FROM customers
GROUP BY kyc_status
ORDER BY total_customers DESC;