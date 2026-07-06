-- ------------------------------------------------------------------------------
-- SECTION 2: BRANCH OVERVIEW
-- ------------------------------------------------------------------------------


-- Q1. How many branches does the bank operate?
-- Purpose: Calculate the total number of bank branches.

SELECT
    COUNT(*) AS total_branches
FROM branches;


-- Q2. Which state has the highest number of branches?
-- Purpose: Identify the state with the largest branch network.

SELECT
    state,
    COUNT(*) AS total_branches
FROM branches
GROUP BY state
ORDER BY total_branches DESC
LIMIT 1;


-- Q3. Which city has the highest number of branches?
-- Purpose: Identify the city with the highest branch presence.

SELECT
    city,
    COUNT(*) AS total_branches
FROM branches
GROUP BY city
ORDER BY total_branches DESC
LIMIT 1;


-- Q4. How many branches are currently active?
-- Purpose: Count the total number of active bank branches.

SELECT
    COUNT(*) AS active_branches
FROM branches
WHERE branch_status = 'Active';


-- Q5. What is the distribution of branches by branch type?
-- Purpose: Analyze the distribution of branches by type.

SELECT
    branch_type,
    COUNT(*) AS total_branches
FROM branches
GROUP BY branch_type
ORDER BY total_branches DESC;