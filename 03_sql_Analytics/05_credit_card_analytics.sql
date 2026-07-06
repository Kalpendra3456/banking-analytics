-- ------------------------------------------------------------------------------
-- SECTION 2: CREDIT CARD PORTFOLIO OVERVIEW
-- ------------------------------------------------------------------------------


-- Q1. How many credit cards have been issued by the bank?
-- Purpose: Count the total number of credit cards issued.

SELECT
    COUNT(*) AS total_credit_cards
FROM credit_cards;


-- Q2. What is the total credit limit across all credit cards?
-- Purpose: Measure the total credit limit allocated to customers.

SELECT
    SUM(credit_limit) AS total_credit_limit
FROM credit_cards;


-- Q3. What is the average credit limit per credit card?
-- Purpose: Calculate the average credit limit across all credit cards.

SELECT
    ROUND(AVG(credit_limit), 2) AS average_credit_limit
FROM credit_cards;


-- Q4. Which credit card type has the highest number of issued cards?
-- Purpose: Identify the most widely issued credit card type.

SELECT
    card_type,
    COUNT(*) AS total_cards
FROM credit_cards
GROUP BY card_type
ORDER BY total_cards DESC
LIMIT 1;


-- Q5. Which credit card type has the highest total credit limit?
-- Purpose: Identify the card type contributing the highest total credit limit.

SELECT
    card_type,
    SUM(credit_limit) AS total_credit_limit
FROM credit_cards
GROUP BY card_type
ORDER BY total_credit_limit DESC
LIMIT 1;